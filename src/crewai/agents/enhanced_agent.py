"""
Extension de l'agent CrewAI avec des capacités avancées de gestion des prompts
et de mémoire à long terme.
"""

from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from pathlib import Path

from ..agent import Agent
from ..memory.long_term.smart_memory import SmartMemory
from ..prompt_manager import PromptManager, PromptTemplate


class EnhancedAgent(Agent):
    """
    Version améliorée de l'agent CrewAI avec gestion avancée des prompts
    et mémoire à long terme.
    """
    
    prompt_manager: Optional[PromptManager] = None
    memory: Optional[SmartMemory] = None
    
    def __init__(
        self,
        prompt_storage_path: Optional[str] = None,
        memory_storage_path: Optional[str] = None,
        **kwargs
    ):
        """Initialise l'agent avec les capacités étendues."""
        super().__init__(**kwargs)
        
        if prompt_storage_path:
            self.prompt_manager = PromptManager(storage_path=prompt_storage_path)
        
        if memory_storage_path:
            self.memory = SmartMemory(storage_path=memory_storage_path)
    
    def execute_task(self, task: Any, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Exécute une tâche en utilisant les prompts gérés et la mémoire à long terme.
        """
        # Récupérer les souvenirs pertinents si la mémoire est activée
        relevant_memories = []
        if self.memory:
            relevant_memories = self.memory.retrieve(
                query=task.description,
                context=context or {},
                limit=5
            )
        
        # Construire le contexte enrichi
        enriched_context = {
            **(context or {}),
            "relevant_memories": [mem.content for mem in relevant_memories]
        }
        
        # Utiliser un template de prompt s'il existe
        if self.prompt_manager:
            task_template = self.prompt_manager.get_template(task.description)
            if task_template:
                task.description = task_template.format(**enriched_context)
        
        # Exécuter la tâche
        result = super().execute_task(task, enriched_context)
        
        # Stocker le résultat dans la mémoire si activée
        if self.memory:
            self.memory.store(
                content=result,
                importance=0.8,  # Importance par défaut, peut être ajustée
                context={
                    "task": task.description,
                    "agent_role": self.role,
                    **(context or {})
                }
            )
        
        return result
    
    def use_prompt_template(self, name: str, **variables) -> str:
        """Utilise un template de prompt existant."""
        if not self.prompt_manager:
            raise ValueError("Prompt manager not initialized")
            
        template = self.prompt_manager.get_template(name)
        if not template:
            raise KeyError(f"Template '{name}' not found")
            
        return template.format(**variables)
    
    def create_prompt_template(
        self,
        name: str,
        content: str,
        description: Optional[str] = None,
        variables: Optional[List[str]] = None
    ) -> PromptTemplate:
        """Crée un nouveau template de prompt."""
        if not self.prompt_manager:
            raise ValueError("Prompt manager not initialized")
            
        return self.prompt_manager.add_template(
            name=name,
            content=content,
            description=description,
            variables=variables
        )
    
    def remember(
        self,
        content: str,
        importance: float = 0.8,
        context: Optional[Dict[str, Any]] = None
    ) -> str:
        """Stocke une information dans la mémoire à long terme."""
        if not self.memory:
            raise ValueError("Memory system not initialized")
            
        return self.memory.store(
            content=content,
            importance=importance,
            context=context or {}
        ) 