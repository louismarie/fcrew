"""
Core implementation of the Prompt Manager.
"""

from typing import Dict, Optional, List
from pydantic import BaseModel
from pathlib import Path
import json
import os

from .prompt_template import PromptTemplate
from .prompt_version import PromptVersion


class PromptManager(BaseModel):
    """
    A sophisticated prompt management system that handles versioning,
    templating, and dynamic prompt generation.
    """
    
    templates: Dict[str, PromptTemplate] = {}
    storage_path: Optional[Path] = None
    
    def __init__(self, storage_path: Optional[str] = None):
        """Initialize the PromptManager with optional storage path."""
        super().__init__()
        if storage_path:
            self.storage_path = Path(storage_path)
            self.storage_path.mkdir(parents=True, exist_ok=True)
            self._load_templates()
    
    def add_template(self, name: str, content: str, 
                    description: Optional[str] = None,
                    variables: Optional[List[str]] = None) -> PromptTemplate:
        """Add a new prompt template."""
        template = PromptTemplate(
            name=name,
            content=content,
            description=description,
            variables=variables or []
        )
        self.templates[name] = template
        self._save_templates()
        return template
    
    def get_template(self, name: str) -> Optional[PromptTemplate]:
        """Retrieve a prompt template by name."""
        return self.templates.get(name)
    
    def update_template(self, name: str, content: str,
                       description: Optional[str] = None,
                       variables: Optional[List[str]] = None) -> PromptTemplate:
        """Update an existing template and create a new version."""
        if name not in self.templates:
            raise KeyError(f"Template '{name}' not found")
            
        template = self.templates[name]
        template.add_version(content)
        
        if description:
            template.description = description
        if variables:
            template.variables = variables
            
        self._save_templates()
        return template
    
    def _load_templates(self) -> None:
        """Load templates from storage."""
        if not self.storage_path:
            return
            
        template_file = self.storage_path / "templates.json"
        if not template_file.exists():
            return
            
        with open(template_file, "r") as f:
            data = json.load(f)
            for template_data in data:
                template = PromptTemplate.parse_obj(template_data)
                self.templates[template.name] = template
    
    def _save_templates(self) -> None:
        """Save templates to storage."""
        if not self.storage_path:
            return
            
        template_file = self.storage_path / "templates.json"
        with open(template_file, "w") as f:
            json.dump(
                [template.dict() for template in self.templates.values()],
                f,
                indent=2
            ) 