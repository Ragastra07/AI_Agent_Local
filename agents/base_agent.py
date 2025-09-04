from utils.config_loader import ConfigLoader
from llm_config.base_ollama import get_ollama_model


class BaseAgent:
    """
    BaseAgent is the blueprint for all specialized agents.
    Each agent (Jati, Mahoni, Akasia, Beringin) will inherit from this class.
    """

    def __init__(self, agent_name: str):
        # Load configuration
        self.config = ConfigLoader()
        self.agent_name = agent_name

        # Get model name from agent_roles.yaml (or fallback from system_settings.yaml)
        model_name = self.config.get_agent_model(agent_name)

        # Get system settings (temperature, max_tokens, etc.)
        self.system_settings = self.config.get_system_settings()

        # Initialize model dynamically
        self.llm = get_ollama_model(
            model_name,
            temperature=self.system_settings.get("temperature", 0.7),
            max_tokens=self.system_settings.get("max_tokens", 512),
        )

        # Load prompt
        self.system_prompt = self.config.get_agent_prompt(agent_name)

        # Get description from agent_roles.yaml
        self.description = self.config.agent_roles.get(agent_name, {}).get(
            "description", "No description available"
        )

    def introduce(self):
        """
        Introduce the agent using its description from configs.
        """
        return f"I am {self.agent_name}, {self.description}"

    def chat(self, message: str):
        """
        Send a message to the LLM and return its response.
        """
        prompt = f"{self.system_prompt}\n\nUser: {message}\nAgent:"
        return self.llm.invoke(prompt)

    def run_task(self, task: str):
        """
        Placeholder for agent-specific tasks.
        Subclasses can override this method.
        """
        return self.chat(task)