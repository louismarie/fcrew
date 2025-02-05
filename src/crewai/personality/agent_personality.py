"""
Système de gestion de la personnalité et des émotions des agents.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel
from datetime import datetime
import json
import numpy as np

class EmotionalState(BaseModel):
    """État émotionnel de l'agent."""
    joy: float = 0.5
    trust: float = 0.5
    fear: float = 0.0
    surprise: float = 0.0
    sadness: float = 0.0
    disgust: float = 0.0
    anger: float = 0.0
    anticipation: float = 0.5

    def update(self, stimulus: Dict[str, float], intensity: float = 0.1):
        """Met à jour l'état émotionnel en fonction d'un stimulus."""
        for emotion, value in stimulus.items():
            if hasattr(self, emotion):
                current = getattr(self, emotion)
                setattr(self, emotion, 
                       max(0.0, min(1.0, current + value * intensity)))

class PersonalityTrait(BaseModel):
    """Trait de personnalité de l'agent."""
    name: str
    value: float
    description: str

class AgentPersonality(BaseModel):
    """
    Système de personnalité pour les agents FCrew.
    Permet de simuler des traits de caractère et des émotions.
    """
    
    traits: Dict[str, PersonalityTrait] = {
        "openness": PersonalityTrait(
            name="openness",
            value=0.5,
            description="Ouverture aux nouvelles expériences"
        ),
        "conscientiousness": PersonalityTrait(
            name="conscientiousness",
            value=0.5,
            description="Conscience professionnelle"
        ),
        "extraversion": PersonalityTrait(
            name="extraversion",
            value=0.5,
            description="Extraversion"
        ),
        "agreeableness": PersonalityTrait(
            name="agreeableness",
            value=0.5,
            description="Agréabilité"
        ),
        "neuroticism": PersonalityTrait(
            name="neuroticism",
            value=0.5,
            description="Névrosisme"
        )
    }
    
    emotional_state: EmotionalState = EmotionalState()
    emotional_history: List[Dict] = []
    
    def adjust_response(self, response: str) -> str:
        """Ajuste la réponse en fonction de la personnalité et des émotions."""
        # Influence de l'extraversion
        if self.traits["extraversion"].value > 0.7:
            response = response.replace(".", "!")
            response = f"😊 {response}"
        elif self.traits["extraversion"].value < 0.3:
            response = response.replace("!", ".")
            response = response.strip("!") + "..."
        
        # Influence de l'ouverture
        if self.traits["openness"].value > 0.7:
            response = f"{response}\n\nD'ailleurs, cela me fait penser à..."
        
        # Influence des émotions
        if self.emotional_state.joy > 0.7:
            response = f"Je suis ravi de vous dire que {response} 🌟"
        elif self.emotional_state.sadness > 0.7:
            response = f"Malheureusement, {response} 😔"
        
        return response
    
    def process_interaction(self, interaction: str):
        """Traite une interaction et met à jour l'état émotionnel."""
        # Analyse simple des mots-clés pour les émotions
        positive_words = ["excellent", "super", "bravo", "merci"]
        negative_words = ["erreur", "problème", "mauvais", "échec"]
        
        stimulus = {
            "joy": sum(word in interaction.lower() for word in positive_words) * 0.2,
            "sadness": sum(word in interaction.lower() for word in negative_words) * 0.2
        }
        
        self.emotional_state.update(stimulus)
        self.emotional_history.append({
            "timestamp": datetime.utcnow().isoformat(),
            "interaction": interaction,
            "emotional_state": self.emotional_state.dict()
        })
    
    def get_personality_influence(self) -> Dict[str, float]:
        """Calcule l'influence de la personnalité sur le comportement."""
        return {
            "creativity": (self.traits["openness"].value * 0.7 + 
                         self.emotional_state.joy * 0.3),
            "detail_focus": (self.traits["conscientiousness"].value * 0.8 + 
                           self.emotional_state.trust * 0.2),
            "collaboration": (self.traits["agreeableness"].value * 0.6 + 
                            self.emotional_state.trust * 0.4),
            "risk_taking": (self.traits["extraversion"].value * 0.5 + 
                          self.emotional_state.anticipation * 0.5)
        }
    
    def save_state(self, file_path: str):
        """Sauvegarde l'état de la personnalité."""
        with open(file_path, 'w') as f:
            json.dump({
                "traits": {k: v.dict() for k, v in self.traits.items()},
                "emotional_state": self.emotional_state.dict(),
                "emotional_history": self.emotional_history
            }, f, indent=2)
    
    def load_state(self, file_path: str):
        """Charge l'état de la personnalité."""
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.traits = {
                k: PersonalityTrait(**v) for k, v in data["traits"].items()
            }
            self.emotional_state = EmotionalState(**data["emotional_state"])
            self.emotional_history = data["emotional_history"] 