"""
Système de collaboration avancée pour les agents FCrew.
"""

from typing import Dict, List, Optional, Set
from pydantic import BaseModel
from datetime import datetime
import networkx as nx
import json

class Skill(BaseModel):
    """Représente une compétence d'agent."""
    name: str
    level: float  # 0.0 à 1.0
    description: str
    tags: List[str] = []

class CollaborationLink(BaseModel):
    """Représente un lien de collaboration entre agents."""
    agent_from: str
    agent_to: str
    strength: float  # 0.0 à 1.0
    last_interaction: datetime
    successful_collaborations: int = 0
    failed_collaborations: int = 0

class CollaborationNetwork(BaseModel):
    """
    Réseau de collaboration entre agents.
    Gère les relations, compétences et synergies.
    """
    
    agents: Dict[str, Dict[str, Skill]] = {}
    links: List[CollaborationLink] = []
    teams: Dict[str, List[str]] = {}
    
    def __init__(self, **data):
        """Initialise le réseau de collaboration."""
        super().__init__(**data)
        self._graph = nx.DiGraph()
    
    def add_agent(self, agent_id: str, skills: Dict[str, Skill]):
        """Ajoute un agent au réseau."""
        self.agents[agent_id] = skills
        self._graph.add_node(agent_id, skills=skills)
    
    def add_collaboration(
        self,
        agent_from: str,
        agent_to: str,
        strength: float = 0.5
    ):
        """Ajoute ou met à jour un lien de collaboration."""
        link = CollaborationLink(
            agent_from=agent_from,
            agent_to=agent_to,
            strength=strength,
            last_interaction=datetime.utcnow()
        )
        self.links.append(link)
        self._graph.add_edge(
            agent_from,
            agent_to,
            weight=strength,
            link=link
        )
    
    def update_collaboration(
        self,
        agent_from: str,
        agent_to: str,
        success: bool
    ):
        """Met à jour les statistiques de collaboration."""
        for link in self.links:
            if (link.agent_from == agent_from and
                link.agent_to == agent_to):
                if success:
                    link.successful_collaborations += 1
                    link.strength = min(1.0, link.strength + 0.1)
                else:
                    link.failed_collaborations += 1
                    link.strength = max(0.0, link.strength - 0.1)
                link.last_interaction = datetime.utcnow()
                break
    
    def find_best_collaborator(
        self,
        agent_id: str,
        required_skills: List[str]
    ) -> Optional[str]:
        """Trouve le meilleur collaborateur pour une tâche donnée."""
        if agent_id not in self.agents:
            return None
            
        best_score = 0.0
        best_collaborator = None
        
        for potential_id, skills in self.agents.items():
            if potential_id == agent_id:
                continue
                
            # Calcul du score basé sur les compétences et la force du lien
            skill_score = sum(
                skills.get(skill, Skill(name=skill, level=0.0, description="")).level
                for skill in required_skills
            ) / len(required_skills)
            
            # Trouver le lien de collaboration s'il existe
            collaboration_strength = 0.5  # valeur par défaut
            for link in self.links:
                if (link.agent_from == agent_id and
                    link.agent_to == potential_id):
                    collaboration_strength = link.strength
                    break
            
            total_score = skill_score * 0.7 + collaboration_strength * 0.3
            
            if total_score > best_score:
                best_score = total_score
                best_collaborator = potential_id
        
        return best_collaborator
    
    def create_optimal_team(
        self,
        task_requirements: Dict[str, float],
        team_size: int
    ) -> List[str]:
        """Crée une équipe optimale pour une tâche donnée."""
        team = []
        remaining_skills = task_requirements.copy()
        
        while len(team) < team_size and remaining_skills:
            best_agent = None
            best_score = 0.0
            
            for agent_id, skills in self.agents.items():
                if agent_id in team:
                    continue
                
                # Calcul du score de contribution
                score = 0.0
                for skill_name, required_level in remaining_skills.items():
                    if skill_name in skills:
                        score += min(skills[skill_name].level,
                                   required_level)
                
                # Bonus pour la collaboration avec l'équipe existante
                if team:
                    collaboration_score = 0.0
                    for team_member in team:
                        for link in self.links:
                            if ((link.agent_from == agent_id and
                                 link.agent_to == team_member) or
                                (link.agent_from == team_member and
                                 link.agent_to == agent_id)):
                                collaboration_score += link.strength
                    score += collaboration_score / len(team) * 0.3
                
                if score > best_score:
                    best_score = score
                    best_agent = agent_id
            
            if best_agent:
                team.append(best_agent)
                # Mettre à jour les compétences restantes nécessaires
                for skill_name in list(remaining_skills.keys()):
                    if skill_name in self.agents[best_agent]:
                        remaining_skills[skill_name] = max(
                            0.0,
                            remaining_skills[skill_name] -
                            self.agents[best_agent][skill_name].level
                        )
                        if remaining_skills[skill_name] == 0.0:
                            del remaining_skills[skill_name]
            else:
                break
        
        return team
    
    def analyze_network(self) -> Dict:
        """Analyse le réseau de collaboration."""
        return {
            "density": nx.density(self._graph),
            "centrality": nx.degree_centrality(self._graph),
            "communities": list(nx.community.greedy_modularity_communities(
                self._graph.to_undirected()
            )),
            "average_clustering": nx.average_clustering(
                self._graph.to_undirected()
            )
        }
    
    def save_network(self, file_path: str):
        """Sauvegarde le réseau de collaboration."""
        with open(file_path, 'w') as f:
            json.dump({
                "agents": {
                    agent_id: {
                        skill_name: skill.dict()
                        for skill_name, skill in skills.items()
                    }
                    for agent_id, skills in self.agents.items()
                },
                "links": [link.dict() for link in self.links],
                "teams": self.teams
            }, f, indent=2)
    
    def load_network(self, file_path: str):
        """Charge le réseau de collaboration."""
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.agents = {
                agent_id: {
                    skill_name: Skill(**skill_data)
                    for skill_name, skill_data in skills.items()
                }
                for agent_id, skills in data["agents"].items()
            }
            self.links = [CollaborationLink(**link) for link in data["links"]]
            self.teams = data["teams"]
            
            # Reconstruire le graphe
            self._graph = nx.DiGraph()
            for agent_id, skills in self.agents.items():
                self._graph.add_node(agent_id, skills=skills)
            for link in self.links:
                self._graph.add_edge(
                    link.agent_from,
                    link.agent_to,
                    weight=link.strength,
                    link=link
                ) 