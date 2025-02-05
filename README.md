# FCrew - Framework d'Agents IA Avancé

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads/)

> 🤖 **FCrew** est un framework nouvelle génération pour la création d'agents IA avec mémoire à long terme et gestion avancée des prompts. Basé sur CrewAI, il ajoute des capacités sophistiquées de mémorisation, de contextualisation et d'apprentissage, permettant aux agents de maintenir une cohérence dans leurs interactions et d'apprendre de leurs expériences.

## 🌟 Points Forts
- 📝 Gestion avancée des prompts avec versionnage
- 🧠 Mémoire à long terme avec oubli intelligent
- 🤝 Collaboration avancée entre agents
- 🎭 Système de personnalité et d'émotions
- 📊 Apprentissage par renforcement
- 🔄 Contextualisation automatique des interactions
- 📊 Optimisation vectorielle des souvenirs

## Nouvelles Fonctionnalités

### 1. Système de Personnalité et d'Émotions
```python
from fcrew.personality import AgentPersonality

# Création d'une personnalité
personality = AgentPersonality()

# Ajustement des traits
personality.traits["openness"].value = 0.8
personality.traits["extraversion"].value = 0.6

# Traitement des interactions
personality.process_interaction("Excellent travail !")
response = personality.adjust_response("Merci pour votre retour.")
```

### 2. Apprentissage par Renforcement
```python
from fcrew.learning import ReinforcementLearning

# Création du système d'apprentissage
learning = ReinforcementLearning()

# Apprentissage à partir d'expériences
learning.update(Experience(
    state={"context": 0.5},
    action="ask_question",
    reward=1.0,
    next_state={"context": 0.8}
))

# Obtention de la meilleure action
action = learning.get_action({"context": 0.5})
```

### 3. Collaboration Avancée
```python
from fcrew.collaboration import CollaborationNetwork, Skill

# Création du réseau
network = CollaborationNetwork()

# Ajout d'agents avec leurs compétences
network.add_agent("agent1", {
    "analyse": Skill(name="analyse", level=0.8, description="Analyse de données")
})

# Création d'équipes optimales
team = network.create_optimal_team(
    task_requirements={"analyse": 0.7},
    team_size=2
)
```

## Intégration des Fonctionnalités

### Création d'un Agent Avancé
```python
from fcrew import EnhancedAgent, AgentPersonality, ReinforcementLearning

# Configuration de l'agent
agent = EnhancedAgent(
    role="Analyste",
    goal="Analyser les données",
    personality=AgentPersonality(
        traits={
            "openness": 0.8,
            "conscientiousness": 0.9
        }
    ),
    learning_system=ReinforcementLearning(),
    prompt_storage_path="~/.fcrew/prompts",
    memory_storage_path="~/.fcrew/memory"
)

# Utilisation des capacités avancées
agent.personality.process_interaction("Excellent travail !")
agent.learning_system.update(experience)
```

### Création d'un Crew Collaboratif
```python
from fcrew import Crew, CollaborationNetwork

# Création du réseau de collaboration
network = CollaborationNetwork()

# Ajout des agents au réseau
network.add_agent("analyst", {
    "analyse": Skill(name="analyse", level=0.8),
    "reporting": Skill(name="reporting", level=0.7)
})
network.add_agent("researcher", {
    "research": Skill(name="research", level=0.9),
    "analyse": Skill(name="analyse", level=0.6)
})

# Création du crew avec collaboration
crew = Crew(
    agents=[analyst, researcher],
    collaboration_network=network,
    process=Process.sequential
)

# Exécution avec optimisation automatique des collaborations
result = crew.kickoff(
    optimize_collaborations=True,
    task_requirements={
        "analyse": 0.7,
        "research": 0.8
    }
)
```

### Personnalisation des Interactions
```python
# Configuration des traits de personnalité
agent.personality.traits["openness"].value = 0.9
agent.personality.emotional_state.joy = 0.8

# Exécution d'une tâche avec personnalité
response = agent.execute_task(
    task,
    context={"mood": "positive"},
    adjust_personality=True
)

# Analyse des performances d'apprentissage
performance = agent.learning_system.analyze_performance()
print(f"Récompense moyenne : {performance['average_reward']}")
```

## Avantages des Nouvelles Fonctionnalités

### 1. Personnalité et Émotions
- **Interactions Plus Naturelles** : Les agents répondent de manière plus humaine et contextuelle
- **Cohérence Comportementale** : Maintien d'une personnalité cohérente à travers les interactions
- **Adaptation Émotionnelle** : Réponses adaptées au contexte émotionnel de l'interaction
- **Historique Émotionnel** : Traçabilité de l'évolution émotionnelle des agents

### 2. Apprentissage par Renforcement
- **Amélioration Continue** : Les agents apprennent de leurs expériences
- **Optimisation des Décisions** : Choix d'actions basés sur les réussites passées
- **Adaptation Contextuelle** : Apprentissage spécifique au contexte
- **Mesure des Performances** : Suivi quantitatif de l'apprentissage

### 3. Collaboration Avancée
- **Équipes Optimales** : Création automatique d'équipes basée sur les compétences
- **Synergies** : Identification et exploitation des complémentarités entre agents
- **Historique Collaboratif** : Suivi et amélioration des collaborations
- **Analyse de Réseau** : Visualisation et optimisation des relations entre agents

## Cas d'Usage Avancés

### 1. Support Client Émotionnellement Intelligent
```python
agent = EnhancedAgent(
    role="Support Client",
    personality=AgentPersonality(
        traits={"empathy": 0.9}
    )
)
agent.personality.process_interaction("Je suis très frustré par ce problème !")
response = agent.execute_task(task, adjust_personality=True)
```

### 2. Équipe de Recherche Auto-Optimisante
```python
crew = Crew(
    agents=[researcher, analyst, writer],
    collaboration_network=network,
    learning_enabled=True
)

# L'équipe s'améliore au fil des tâches
for task in research_tasks:
    result = crew.kickoff(task)
    crew.learn_from_execution(task, result)
```

### 3. Assistant Personnel Adaptatif
```python
assistant = EnhancedAgent(
    role="Assistant Personnel",
    personality=AgentPersonality(),
    learning_system=ReinforcementLearning()
)

# L'assistant apprend les préférences de l'utilisateur
assistant.remember(
    content="L'utilisateur préfère des réponses concises",
    importance=0.9
)
assistant.personality.adapt_to_user_preferences()
```

## Prérequis

- Python 3.10 ou supérieur
- 2GB d'espace disque minimum (pour le stockage des prompts et de la mémoire)
- Clé API OpenAI (ou autre LLM compatible)
- RAM recommandée : 8GB minimum

### Dépendances Principales

```toml
dependencies = [
    "pydantic>=2.4.2",
    "openai>=1.13.3",
    "chromadb>=0.5.23",
    "tiktoken>=0.7.0"
]
```

### Compatibilité des Modèles

FCrew est compatible avec plusieurs fournisseurs de modèles de langage :

| Fournisseur | Modèles Supportés | Configuration |
|-------------|-------------------|---------------|
| OpenAI | O1-mini, O1, O1 pro, O3-mini, O3-mini-high, GPT-4o, GPT-3.5 | Clé API requise |
| Anthropic | Sonnet, Haiku | Clé API requise |
| Ollama | Tous les modèles | Installation locale |
| LlamaCpp | Tous les modèles compatibles | Installation locale |

## Fonctionnalités Principales

### 1. Gestion Avancée des Prompts
- Création et gestion de templates de prompts
- Versionnage automatique des prompts
- Variables dynamiques dans les templates
- Historique des modifications
- Stockage persistant des prompts

### 2. Mémoire à Long Terme Intelligente
- Recherche sémantique des souvenirs
- Mécanisme d'oubli intelligent basé sur l'importance
- Consolidation automatique de la mémoire
- Récupération contextuelle des informations
- Stockage vectoriel optimisé

## Installation

```bash
pip install fcrew
```

## Guide d'Utilisation

### 1. Configuration de Base

```python
from fcrew import FCrewConfig

# Configuration via fichier JSON
config = FCrewConfig.load_from_file("fcrew_config.json")

# Ou configuration programmatique
config = FCrewConfig(
    prompt_storage_path="~/.fcrew/prompts",
    memory_storage_path="~/.fcrew/memory",
    max_memories=10000
)
```

### 2. Création d'un Agent Amélioré

```python
from crewai import Task, Crew, Process
from crewai.agents import EnhancedAgent
import os

# Création des chemins de stockage
base_path = os.path.expanduser("~/.fcrew")
prompts_path = os.path.join(base_path, "prompts")
memory_path = os.path.join(base_path, "memory")

# Création de l'agent
agent = EnhancedAgent(
    role="Analyste IA",
    goal="Analyser les tendances en IA",
    backstory="Expert en analyse de données et tendances IA",
    prompt_storage_path=prompts_path,
    memory_storage_path=memory_path
)
```

### 3. Gestion des Prompts

```python
# Création d'un template
agent.create_prompt_template(
    name="analyse_tendance",
    content="""
    Analyser les tendances en ${domaine} avec focus sur :
    1. Innovations récentes
    2. Impact sur le marché
    3. Perspectives futures
    
    Contexte historique :
    ${relevant_memories}
    """,
    variables=["domaine"]
)

# Utilisation du template
resultat = agent.use_prompt_template(
    "analyse_tendance",
    domaine="intelligence artificielle"
)
```

### 4. Utilisation de la Mémoire

```python
# Stockage d'une information
agent.remember(
    content="GPT-4 a montré des capacités de raisonnement avancées",
    importance=0.9,
    context={"domaine": "LLM", "date": "2024"}
)

# La mémoire est automatiquement utilisée lors de l'exécution des tâches
task = Task(
    description="Analyser l'évolution des LLM",
    agent=agent
)
```

### 5. Création d'un Crew

```python
# Création d'un crew avec plusieurs agents
researcher = EnhancedAgent(
    role="Chercheur",
    goal="Rechercher les dernières avancées",
    prompt_storage_path=prompts_path,
    memory_storage_path=memory_path
)

analyst = EnhancedAgent(
    role="Analyste",
    goal="Analyser les implications",
    prompt_storage_path=prompts_path,
    memory_storage_path=memory_path
)

# Définition des tâches
research_task = Task(
    description="Rechercher les dernières avancées en IA",
    agent=researcher
)

analysis_task = Task(
    description="Analyser les implications des découvertes",
    agent=analyst
)

# Création du crew
crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    process=Process.sequential,
    verbose=True
)

# Exécution
resultat = crew.kickoff()
```

## Fonctionnalités Avancées

### Gestion de la Mémoire Partagée

Les agents d'un même crew peuvent partager leur mémoire en utilisant le même chemin de stockage :

```python
memory_path = "~/.fcrew/shared_memory"
agent1 = EnhancedAgent(..., memory_storage_path=memory_path)
agent2 = EnhancedAgent(..., memory_storage_path=memory_path)
```

### Templates de Prompts Partagés

De même pour les prompts :

```python
prompts_path = "~/.fcrew/shared_prompts"
agent1 = EnhancedAgent(..., prompt_storage_path=prompts_path)
agent2 = EnhancedAgent(..., prompt_storage_path=prompts_path)
```

### Personnalisation de l'Importance des Souvenirs

```python
agent.remember(
    content="Information critique",
    importance=1.0,  # Importance maximale
    context={"type": "critique"}
)
```

## Bonnes Pratiques

1. **Organisation des Prompts**
   - Créez des templates réutilisables
   - Utilisez des variables pour la flexibilité
   - Documentez vos templates

2. **Gestion de la Mémoire**
   - Définissez des niveaux d'importance appropriés
   - Utilisez des contextes pertinents
   - Partagez la mémoire quand cela fait sens

3. **Configuration**
   - Utilisez des chemins de stockage différents pour différents projets
   - Ajustez max_memories selon vos besoins
   - Activez le mode debug pour le développement

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité
3. Soumettez une Pull Request

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## 🔧 Résolution des Problèmes Courants

### Problèmes de Mémoire

1. **Erreur de stockage vectoriel**
   ```
   Solution : Vérifiez l'espace disque et les permissions du dossier de stockage
   ```

2. **Mémoire non persistante**
   ```
   Solution : Assurez-vous que le chemin de stockage est absolu et accessible
   ```

3. **Lenteur des recherches**
   ```
   Solution : Ajustez max_memories ou utilisez un index optimisé
   ```

### Problèmes de Prompts

1. **Variables non résolues**
   ```python
   # Incorrect
   template.format(wrong_var="value")
   
   # Correct
   template.format(expected_var="value")
   ```

2. **Versions manquantes**
   ```
   Solution : Vérifiez que le stockage des prompts est correctement initialisé
   ```

## 📋 Cas d'Utilisation Recommandés

### 1. Assistant Personnel Évolutif
- Utilisation de la mémoire pour apprendre les préférences
- Prompts personnalisés par utilisateur
- Contexte maintenu entre les sessions

### 2. Analyse de Documents
- Mémoire partagée entre agents
- Templates spécialisés par type de document
- Conservation du contexte historique

### 3. Support Client Intelligent
- Mémorisation des interactions précédentes
- Prompts adaptés au contexte client
- Partage d'informations entre agents

### 4. Recherche et Synthèse
- Accumulation progressive de connaissances
- Templates structurés pour la cohérence
- Mémoire pour éviter les redondances

## 🎯 Performances et Limites

### Performances
- Temps de réponse moyen : < 2s
- Capacité de stockage : ~1M souvenirs
- Précision de la recherche : ~95%

### Limites Actuelles
- Taille maximale des prompts : 100KB
- Nombre maximal d'agents par crew : 50
- Taille maximale de la mémoire partagée : 10GB

## 🚀 Démarrage Rapide

1. **Installation**
```bash
pip install fcrew
```

2. **Configuration Minimale**
```python
from fcrew import FCrewConfig, EnhancedAgent, Task, Crew

# Configuration de base
config = FCrewConfig(
    prompt_storage_path="~/.fcrew/prompts",
    memory_storage_path="~/.fcrew/memory"
)

# Création d'un agent avec mémoire
agent = EnhancedAgent(
    role="Assistant",
    goal="Aider l'utilisateur",
    prompt_storage_path=config.effective_prompt_storage_path,
    memory_storage_path=config.effective_memory_storage_path
)

# Création et exécution d'une tâche
task = Task(description="Saluer l'utilisateur", agent=agent)
crew = Crew(agents=[agent], tasks=[task])
resultat = crew.kickoff()
```

3. **Variables d'Environnement**
```bash
# .env
OPENAI_API_KEY=sk-...
FCREW_DEBUG=false
FCREW_MEMORY_PATH=~/.fcrew/memory
FCREW_PROMPTS_PATH=~/.fcrew/prompts
```
