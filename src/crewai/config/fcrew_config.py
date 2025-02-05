"""
Configuration settings for FCrew.
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel
from pathlib import Path
import json
import os


class FCrewConfig(BaseModel):
    """Configuration settings for FCrew."""
    
    # Prompt Manager Settings
    prompt_storage_path: Optional[str] = None
    default_prompt_variables: Dict[str, Any] = {}
    
    # Memory Settings
    memory_storage_path: Optional[str] = None
    max_memories: int = 10000
    memory_importance_threshold: float = 0.5
    
    # General Settings
    debug_mode: bool = False
    telemetry_enabled: bool = True
    
    @classmethod
    def load_from_file(cls, config_path: str) -> 'FCrewConfig':
        """Load configuration from a JSON file."""
        path = Path(config_path)
        if not path.exists():
            return cls()
            
        with open(path, 'r') as f:
            config_data = json.load(f)
            return cls(**config_data)
    
    def save_to_file(self, config_path: str):
        """Save configuration to a JSON file."""
        path = Path(config_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w') as f:
            json.dump(self.dict(), f, indent=2)
    
    @property
    def effective_prompt_storage_path(self) -> str:
        """Get the effective prompt storage path."""
        if self.prompt_storage_path:
            return self.prompt_storage_path
            
        default_path = os.path.expanduser("~/.fcrew/prompts")
        os.makedirs(default_path, exist_ok=True)
        return default_path
    
    @property
    def effective_memory_storage_path(self) -> str:
        """Get the effective memory storage path."""
        if self.memory_storage_path:
            return self.memory_storage_path
            
        default_path = os.path.expanduser("~/.fcrew/memory")
        os.makedirs(default_path, exist_ok=True)
        return default_path 