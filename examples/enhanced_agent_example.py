"""
Exemple d'utilisation de l'agent amélioré avec gestion des prompts
et mémoire à long terme.
"""

from crewai import Task, Crew, Process
from crewai.agents import EnhancedAgent
import os

def main():
    # Création des chemins de stockage
    base_path = os.path.expanduser("~/.fcrew")
    prompts_path = os.path.join(base_path, "prompts")
    memory_path = os.path.join(base_path, "memory")
    
    # Création de l'agent amélioré
    researcher = EnhancedAgent(
        role="Chercheur en IA",
        goal="Analyser et synthétiser les dernières avancées en IA",
        backstory="Vous êtes un chercheur expérimenté spécialisé dans l'IA",
        prompt_storage_path=prompts_path,
        memory_storage_path=memory_path
    )
    
    # Création d'un template de prompt
    researcher.create_prompt_template(
        name="analyse_ia",
        content="""
        En tant que chercheur en IA, analysez les développements récents en ${domaine}.
        
        Contexte historique :
        ${relevant_memories}
        
        Points à couvrir :
        1. Innovations majeures
        2. Implications pratiques
        3. Défis et limitations
        4. Perspectives futures
        """,
        variables=["domaine"]
    )
    
    # Création d'une tâche
    task = Task(
        description="analyse_ia",  # Correspond au nom du template
        agent=researcher
    )
    
    # Création et exécution du crew
    crew = Crew(
        agents=[researcher],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )
    
    # Exécution avec le contexte
    result = crew.kickoff(
        inputs={
            "domaine": "apprentissage par renforcement"
        }
    )
    
    print("\nRésultat de l'analyse :")
    print(result)

if __name__ == "__main__":
    main() 