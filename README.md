# FCrew - Advanced AI Agents Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads/)

> 🤖 **FCrew** is a next-generation framework for creating AI agents with long-term memory and advanced prompt management. Based on CrewAI, it adds sophisticated memory, contextualization, and learning capabilities, allowing agents to maintain consistency in their interactions and learn from their experiences.

## 🌟 Key Features
- 📝 Advanced prompt management with versioning
- 🧠 Long-term memory with intelligent forgetting
- 🤝 Advanced agent collaboration
- 🎭 Personality and emotion system
- 📊 Reinforcement learning
- 🔄 Automatic interaction contextualization
- 📊 Vector memory optimization

## New Features

### 1. Personality and Emotion System
```python
from fcrew.personality import AgentPersonality

# Create a personality
personality = AgentPersonality()

# Adjust traits
personality.traits["openness"].value = 0.8
personality.traits["extraversion"].value = 0.6

# Process interactions
personality.process_interaction("Excellent work!")
response = personality.adjust_response("Thank you for your feedback.")
```

### 2. Reinforcement Learning
```python
from fcrew.learning import ReinforcementLearning

# Create learning system
learning = ReinforcementLearning()

# Learn from experiences
learning.update(Experience(
    state={"context": 0.5},
    action="ask_question",
    reward=1.0,
    next_state={"context": 0.8}
))

# Get best action
action = learning.get_action({"context": 0.5})
```

### 3. Advanced Collaboration
```python
from fcrew.collaboration import CollaborationNetwork, Skill

# Create network
network = CollaborationNetwork()

# Add agents with their skills
network.add_agent("agent1", {
    "analysis": Skill(name="analysis", level=0.8, description="Data analysis")
})

# Create optimal teams
team = network.create_optimal_team(
    task_requirements={"analysis": 0.7},
    team_size=2
)
```

## Feature Integration

### Creating an Advanced Agent
```python
from fcrew import EnhancedAgent, AgentPersonality, ReinforcementLearning

# Agent configuration
agent = EnhancedAgent(
    role="Analyst",
    goal="Analyze data",
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

# Use advanced capabilities
agent.personality.process_interaction("Excellent work!")
agent.learning_system.update(experience)
```

### Creating a Collaborative Crew
```python
from fcrew import Crew, CollaborationNetwork

# Create collaboration network
network = CollaborationNetwork()

# Add agents to network
network.add_agent("analyst", {
    "analysis": Skill(name="analysis", level=0.8),
    "reporting": Skill(name="reporting", level=0.7)
})
network.add_agent("researcher", {
    "research": Skill(name="research", level=0.9),
    "analysis": Skill(name="analysis", level=0.6)
})

# Create crew with collaboration
crew = Crew(
    agents=[analyst, researcher],
    collaboration_network=network,
    process=Process.sequential
)

# Execute with automatic collaboration optimization
result = crew.kickoff(
    optimize_collaborations=True,
    task_requirements={
        "analysis": 0.7,
        "research": 0.8
    }
)
```

### Interaction Customization
```python
# Configure personality traits
agent.personality.traits["openness"].value = 0.9
agent.personality.emotional_state.joy = 0.8

# Execute task with personality
response = agent.execute_task(
    task,
    context={"mood": "positive"},
    adjust_personality=True
)

# Analyze learning performance
performance = agent.learning_system.analyze_performance()
print(f"Average reward: {performance['average_reward']}")
```

## Benefits of New Features

### 1. Personality and Emotions
- **More Natural Interactions**: Agents respond in a more human and contextual way
- **Behavioral Consistency**: Maintains consistent personality across interactions
- **Emotional Adaptation**: Responses adapted to interaction's emotional context
- **Emotional History**: Traceability of agents' emotional evolution

### 2. Reinforcement Learning
- **Continuous Improvement**: Agents learn from their experiences
- **Decision Optimization**: Action choices based on past successes
- **Contextual Adaptation**: Context-specific learning
- **Performance Measurement**: Quantitative learning tracking

### 3. Advanced Collaboration
- **Optimal Teams**: Automatic team creation based on skills
- **Synergies**: Identification and exploitation of agent complementarities
- **Collaborative History**: Tracking and improving collaborations
- **Network Analysis**: Visualization and optimization of agent relationships

## Advanced Use Cases

### 1. Emotionally Intelligent Customer Support
```python
agent = EnhancedAgent(
    role="Customer Support",
    personality=AgentPersonality(
        traits={"empathy": 0.9}
    )
)
agent.personality.process_interaction("I'm very frustrated with this problem!")
response = agent.execute_task(task, adjust_personality=True)
```

### 2. Self-Optimizing Research Team
```python
crew = Crew(
    agents=[researcher, analyst, writer],
    collaboration_network=network,
    learning_enabled=True
)

# Team improves over tasks
for task in research_tasks:
    result = crew.kickoff(task)
    crew.learn_from_execution(task, result)
```

### 3. Adaptive Personal Assistant
```python
assistant = EnhancedAgent(
    role="Personal Assistant",
    personality=AgentPersonality(),
    learning_system=ReinforcementLearning()
)

# Assistant learns user preferences
assistant.remember(
    content="User prefers concise responses",
    importance=0.9
)
assistant.personality.adapt_to_user_preferences()
```

## Prerequisites

- Python 3.10 or higher
- 2GB minimum disk space (for prompt and memory storage)
- OpenAI API key (or other compatible LLM)
- Recommended RAM: 8GB minimum

### Main Dependencies

```toml
dependencies = [
    "pydantic>=2.4.2",
    "openai>=1.13.3",
    "chromadb>=0.5.23",
    "tiktoken>=0.7.0"
]
```

### Model Compatibility

FCrew is compatible with several language model providers:

| Provider | Supported Models | Configuration |
|----------|-----------------|---------------|
| OpenAI | O1-mini, O1, O1 pro, O3-mini, O3-mini-high, GPT-4o, GPT-3.5 | API key required |
| Anthropic | Sonnet, Haiku | API key required |
| Ollama | All models | Local installation |
| LlamaCpp | All compatible models | Local installation |

## Core Features

### 1. Advanced Prompt Management
- Creation and management of prompt templates
- Automatic prompt versioning
- Dynamic variables in templates
- Change history
- Persistent prompt storage

### 2. Intelligent Long-term Memory
- Semantic memory search
- Intelligent forgetting mechanism based on importance
- Automatic memory consolidation
- Contextual information retrieval
- Optimized vector storage

## Installation

```bash
pip install fcrew
```

## Usage Guide

### 1. Basic Configuration

```python
from fcrew import FCrewConfig

# Configuration via JSON file
config = FCrewConfig.load_from_file("fcrew_config.json")

# Or programmatic configuration
config = FCrewConfig(
    prompt_storage_path="~/.fcrew/prompts",
    memory_storage_path="~/.fcrew/memory",
    max_memories=10000
)
```

### 2. Creating an Enhanced Agent

```python
from crewai import Task, Crew, Process
from crewai.agents import EnhancedAgent
import os

# Create storage paths
base_path = os.path.expanduser("~/.fcrew")
prompts_path = os.path.join(base_path, "prompts")
memory_path = os.path.join(base_path, "memory")

# Create agent
agent = EnhancedAgent(
    role="AI Analyst",
    goal="Analyze AI trends",
    backstory="Expert in data analysis and AI trends",
    prompt_storage_path=prompts_path,
    memory_storage_path=memory_path
)
```

### 3. Prompt Management

```python
# Create template
agent.create_prompt_template(
    name="trend_analysis",
    content="""
    Analyze trends in ${domain} focusing on:
    1. Recent innovations
    2. Market impact
    3. Future perspectives
    
    Historical context:
    ${relevant_memories}
    """,
    variables=["domain"]
)

# Use template
result = agent.use_prompt_template(
    "trend_analysis",
    domain="artificial intelligence"
)
```

### 4. Using Memory

```python
# Store information
agent.remember(
    content="GPT-4 has shown advanced reasoning capabilities",
    importance=0.9,
    context={"domain": "LLM", "date": "2024"}
)

# Memory is automatically used during task execution
task = Task(
    description="Analyze LLM evolution",
    agent=agent
)
```

### 5. Creating a Crew

```python
# Create crew with multiple agents
researcher = EnhancedAgent(
    role="Researcher",
    goal="Research latest advances",
    prompt_storage_path=prompts_path,
    memory_storage_path=memory_path
)

analyst = EnhancedAgent(
    role="Analyst",
    goal="Analyze implications",
    prompt_storage_path=prompts_path,
    memory_storage_path=memory_path
)

# Define tasks
research_task = Task(
    description="Research latest AI advances",
    agent=researcher
)

analysis_task = Task(
    description="Analyze findings implications",
    agent=analyst
)

# Create crew
crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    process=Process.sequential,
    verbose=True
)

# Execute
result = crew.kickoff()
```

## Advanced Features

### Shared Memory Management

Agents in the same crew can share memory using the same storage path:

```python
memory_path = "~/.fcrew/shared_memory"
agent1 = EnhancedAgent(..., memory_storage_path=memory_path)
agent2 = EnhancedAgent(..., memory_storage_path=memory_path)
```

### Shared Prompt Templates

Similarly for prompts:

```python
prompts_path = "~/.fcrew/shared_prompts"
agent1 = EnhancedAgent(..., prompt_storage_path=prompts_path)
agent2 = EnhancedAgent(..., prompt_storage_path=prompts_path)
```

### Memory Importance Customization

```python
agent.remember(
    content="Critical information",
    importance=1.0,  # Maximum importance
    context={"type": "critical"}
)
```

## Best Practices

1. **Prompt Organization**
   - Create reusable templates
   - Use variables for flexibility
   - Document your templates

2. **Memory Management**
   - Set appropriate importance levels
   - Use relevant contexts
   - Share memory when it makes sense

3. **Configuration**
   - Use different storage paths for different projects
   - Adjust max_memories according to your needs
   - Enable debug mode for development

## Contributing

Contributions are welcome! To contribute:

1. Fork the project
2. Create a feature branch
3. Submit a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔧 Common Problem Resolution

### Memory Issues

1. **Vector storage error**
   ```
   Solution: Check disk space and storage folder permissions
   ```

2. **Non-persistent memory**
   ```
   Solution: Ensure storage path is absolute and accessible
   ```

3. **Slow searches**
   ```
   Solution: Adjust max_memories or use optimized index
   ```

### Prompt Issues

1. **Unresolved variables**
   ```python
   # Incorrect
   template.format(wrong_var="value")
   
   # Correct
   template.format(expected_var="value")
   ```

2. **Missing versions**
   ```
   Solution: Verify prompt storage is properly initialized
   ```

## 📋 Recommended Use Cases

### 1. Evolving Personal Assistant
- Use memory to learn preferences
- Custom prompts per user
- Maintain context between sessions

### 2. Document Analysis
- Shared memory between agents
- Specialized templates per document type
- Historical context preservation

### 3. Intelligent Customer Support
- Remember previous interactions
- Context-adapted prompts
- Information sharing between agents

### 4. Research and Synthesis
- Progressive knowledge accumulation
- Structured templates for consistency
- Memory to avoid redundancy

## 🎯 Performance and Limits

### Performance
- Average response time: < 2s
- Storage capacity: ~1M memories
- Search accuracy: ~95%

### Current Limits
- Maximum prompt size: 100KB
- Maximum agents per crew: 50
- Maximum shared memory size: 10GB

## 🚀 Quick Start

1. **Installation**
```bash
pip install fcrew
```

2. **Minimal Configuration**
```python
from fcrew import FCrewConfig, EnhancedAgent, Task, Crew

# Basic configuration
config = FCrewConfig(
    prompt_storage_path="~/.fcrew/prompts",
    memory_storage_path="~/.fcrew/memory"
)

# Create agent with memory
agent = EnhancedAgent(
    role="Assistant",
    goal="Help user",
    prompt_storage_path=config.effective_prompt_storage_path,
    memory_storage_path=config.effective_memory_storage_path
)

# Create and execute task
task = Task(description="Greet user", agent=agent)
crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

3. **Environment Variables**
```bash
# .env
OPENAI_API_KEY=sk-...
FCREW_DEBUG=false
FCREW_MEMORY_PATH=~/.fcrew/memory
FCREW_PROMPTS_PATH=~/.fcrew/prompts
```
