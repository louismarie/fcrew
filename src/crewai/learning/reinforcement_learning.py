"""
Système d'apprentissage par renforcement pour les agents FCrew.
"""

from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel
import numpy as np
from datetime import datetime
import json
import os

class Experience(BaseModel):
    """Représente une expérience d'apprentissage."""
    state: Dict[str, float]
    action: str
    reward: float
    next_state: Dict[str, float]
    timestamp: datetime

class ReinforcementLearning(BaseModel):
    """
    Système d'apprentissage par renforcement pour les agents FCrew.
    Permet aux agents d'apprendre de leurs interactions et d'améliorer
    leurs décisions au fil du temps.
    """
    
    learning_rate: float = 0.1
    discount_factor: float = 0.95
    exploration_rate: float = 0.2
    min_exploration_rate: float = 0.01
    exploration_decay: float = 0.995
    
    experiences: List[Experience] = []
    q_table: Dict[str, Dict[str, float]] = {}
    action_space: List[str] = []
    
    def __init__(self, **data):
        """Initialise le système d'apprentissage."""
        super().__init__(**data)
        self.action_space = [
            "ask_question",
            "search_memory",
            "create_summary",
            "delegate_task",
            "request_clarification",
            "propose_solution"
        ]
        
    def state_to_key(self, state: Dict[str, float]) -> str:
        """Convertit un état en clé pour la Q-table."""
        return json.dumps(sorted(state.items()))
    
    def get_action(self, state: Dict[str, float]) -> str:
        """
        Sélectionne une action en utilisant la politique epsilon-greedy.
        """
        if np.random.random() < self.exploration_rate:
            return np.random.choice(self.action_space)
            
        state_key = self.state_to_key(state)
        if state_key not in self.q_table:
            self.q_table[state_key] = {
                action: 0.0 for action in self.action_space
            }
            
        return max(self.q_table[state_key].items(),
                  key=lambda x: x[1])[0]
    
    def update(self, experience: Experience):
        """
        Met à jour la Q-table avec une nouvelle expérience.
        """
        state_key = self.state_to_key(experience.state)
        next_state_key = self.state_to_key(experience.next_state)
        
        # Initialiser les états s'ils n'existent pas
        if state_key not in self.q_table:
            self.q_table[state_key] = {
                action: 0.0 for action in self.action_space
            }
        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = {
                action: 0.0 for action in self.action_space
            }
        
        # Q-learning update
        current_q = self.q_table[state_key][experience.action]
        next_max_q = max(self.q_table[next_state_key].values())
        
        new_q = current_q + self.learning_rate * (
            experience.reward +
            self.discount_factor * next_max_q -
            current_q
        )
        
        self.q_table[state_key][experience.action] = new_q
        self.experiences.append(experience)
        
        # Mettre à jour le taux d'exploration
        self.exploration_rate = max(
            self.min_exploration_rate,
            self.exploration_rate * self.exploration_decay
        )
    
    def get_state_value(self, state: Dict[str, float]) -> float:
        """Calcule la valeur d'un état."""
        state_key = self.state_to_key(state)
        if state_key in self.q_table:
            return max(self.q_table[state_key].values())
        return 0.0
    
    def get_best_action_sequence(
        self,
        initial_state: Dict[str, float],
        depth: int = 3
    ) -> List[str]:
        """
        Planifie une séquence d'actions optimale.
        """
        sequence = []
        current_state = initial_state.copy()
        
        for _ in range(depth):
            action = self.get_action(current_state)
            sequence.append(action)
            
            # Simulation simple de l'état suivant
            next_state = current_state.copy()
            next_state["progress"] = min(
                1.0,
                next_state.get("progress", 0) + 0.2
            )
            current_state = next_state
            
        return sequence
    
    def save_model(self, file_path: str):
        """Sauvegarde le modèle d'apprentissage."""
        with open(file_path, 'w') as f:
            json.dump({
                "q_table": self.q_table,
                "exploration_rate": self.exploration_rate,
                "experiences": [exp.dict() for exp in self.experiences]
            }, f, indent=2)
    
    def load_model(self, file_path: str):
        """Charge le modèle d'apprentissage."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.q_table = data["q_table"]
                self.exploration_rate = data["exploration_rate"]
                self.experiences = [
                    Experience(**exp) for exp in data["experiences"]
                ]
    
    def analyze_performance(self) -> Dict[str, float]:
        """Analyse les performances d'apprentissage."""
        if not self.experiences:
            return {}
            
        rewards = [exp.reward for exp in self.experiences]
        return {
            "average_reward": np.mean(rewards),
            "max_reward": max(rewards),
            "min_reward": min(rewards),
            "total_experiences": len(self.experiences),
            "exploration_rate": self.exploration_rate
        } 