"""
Implementation of prompt versioning system.
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PromptVersion(BaseModel):
    """
    Represents a specific version of a prompt template.
    Tracks content, version number, and metadata.
    """
    
    content: str
    version: int
    created_at: datetime
    comment: Optional[str] = None
    
    def __str__(self) -> str:
        """String representation of the version."""
        return f"Version {self.version} ({self.created_at.isoformat()})"
    
    def diff(self, other: 'PromptVersion') -> str:
        """
        Calculate the difference between this version and another.
        Returns a string representation of the changes.
        """
        from difflib import unified_diff
        
        diff = unified_diff(
            self.content.splitlines(keepends=True),
            other.content.splitlines(keepends=True),
            fromfile=f'v{self.version}',
            tofile=f'v{other.version}',
            lineterm=''
        )
        return ''.join(diff) 