"""
Tests pour l'agent amélioré avec gestion des prompts et mémoire à long terme.
"""

import pytest
from pathlib import Path
import tempfile
import shutil
from datetime import datetime

from crewai.agents import EnhancedAgent
from crewai import Task


@pytest.fixture
def temp_storage():
    """Crée un dossier temporaire pour les tests."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


def test_enhanced_agent_initialization(temp_storage):
    """Teste l'initialisation de l'agent amélioré."""
    agent = EnhancedAgent(
        role="Testeur",
        goal="Tester l'agent",
        backstory="Agent de test",
        prompt_storage_path=f"{temp_storage}/prompts",
        memory_storage_path=f"{temp_storage}/memory"
    )
    
    assert agent.prompt_manager is not None
    assert agent.memory is not None
    assert agent.role == "Testeur"


def test_prompt_template_management(temp_storage):
    """Teste la gestion des templates de prompts."""
    agent = EnhancedAgent(
        role="Testeur",
        prompt_storage_path=f"{temp_storage}/prompts"
    )
    
    # Création d'un template
    template = agent.create_prompt_template(
        name="test_template",
        content="Hello ${name}!",
        variables=["name"]
    )
    
    assert template is not None
    assert template.name == "test_template"
    
    # Utilisation du template
    result = agent.use_prompt_template("test_template", name="World")
    assert result == "Hello World!"


def test_memory_storage_and_retrieval(temp_storage):
    """Teste le stockage et la récupération de la mémoire."""
    agent = EnhancedAgent(
        role="Testeur",
        memory_storage_path=f"{temp_storage}/memory"
    )
    
    # Stockage d'une information
    memory_id = agent.remember(
        content="Information importante",
        importance=0.9,
        context={"category": "test"}
    )
    
    assert memory_id is not None
    
    # Récupération via une tâche
    task = Task(
        description="Rechercher des informations importantes",
        agent=agent
    )
    
    result = agent.execute_task(task, {"category": "test"})
    assert "Information importante" in str(result)


def test_task_execution_with_memory_and_prompts(temp_storage):
    """Teste l'exécution d'une tâche avec mémoire et prompts."""
    agent = EnhancedAgent(
        role="Testeur",
        prompt_storage_path=f"{temp_storage}/prompts",
        memory_storage_path=f"{temp_storage}/memory"
    )
    
    # Création d'un template
    agent.create_prompt_template(
        name="task_template",
        content="Analyser: ${topic}\nContexte: ${relevant_memories}",
        variables=["topic"]
    )
    
    # Stockage d'une information en mémoire
    agent.remember(
        content="Donnée historique importante",
        context={"topic": "test"}
    )
    
    # Création et exécution d'une tâche
    task = Task(
        description="task_template",
        agent=agent
    )
    
    result = agent.execute_task(task, {"topic": "test"})
    assert result is not None
    assert isinstance(result, str)


def test_error_handling(temp_storage):
    """Teste la gestion des erreurs."""
    agent = EnhancedAgent(role="Testeur")
    
    # Test d'erreur sans gestionnaire de prompts
    with pytest.raises(ValueError):
        agent.use_prompt_template("nonexistent")
    
    # Test d'erreur sans système de mémoire
    with pytest.raises(ValueError):
        agent.remember("test") 