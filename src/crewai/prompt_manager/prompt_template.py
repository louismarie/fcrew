"""
Implementation of the Prompt Template system.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from datetime import datetime
import string

from .prompt_version import PromptVersion


class PromptTemplate(BaseModel):
    """
    A template for prompts that supports versioning and variable interpolation.
    """
    
    name: str
    content: str
    description: Optional[str] = None
    variables: List[str] = []
    versions: List[PromptVersion] = []
    
    def __init__(self, **data):
        """Initialize the template and create initial version."""
        super().__init__(**data)
        if not self.versions:
            self.add_version(self.content)
    
    def add_version(self, content: str) -> PromptVersion:
        """Add a new version of the template."""
        version = PromptVersion(
            content=content,
            version=len(self.versions) + 1,
            created_at=datetime.utcnow()
        )
        self.versions.append(version)
        self.content = content
        return version
    
    def get_version(self, version: int) -> Optional[PromptVersion]:
        """Get a specific version of the template."""
        try:
            return self.versions[version - 1]
        except IndexError:
            return None
    
    def format(self, **kwargs: Dict[str, Any]) -> str:
        """
        Format the template with the provided variables.
        Validates that all required variables are provided.
        """
        missing_vars = set(self.variables) - set(kwargs.keys())
        if missing_vars:
            raise ValueError(
                f"Missing required variables: {', '.join(missing_vars)}"
            )
            
        template = string.Template(self.content)
        return template.safe_substitute(**kwargs)
    
    def validate_variables(self, variables: Dict[str, Any]) -> bool:
        """Validate that all required variables are present."""
        return set(self.variables).issubset(set(variables.keys()))
