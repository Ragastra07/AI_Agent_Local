import os
import yaml


class ConfigLoader:
    def __init__(self, config_dir="configs"):
        self.config_dir = config_dir
        self.agent_roles = None
        self.prompt_templates = None
        self.system_settings = None
        self.load_all_configs()

    def load_yaml(self, filename):
        """Load a YAML file and return its content as a Python dict"""
        path = os.path.join(self.config_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Config file not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def load_all_configs(self):
        """Load all YAML config files"""
        self.agent_roles = self.load_yaml("agent_roles.yaml")
        self.prompt_templates = self.load_yaml("prompt_templates.yaml")
        self.system_settings = self.load_yaml("system_settings.yaml")

    def get_agent_prompt(self, agent_name):
        """Get the base prompt template for a specific agent"""
        return self.prompt_templates.get(agent_name, {}).get("base_prompt", "")

    def get_agent_model(self, agent_name):
        """Get the default model assigned to a specific agent"""
        return self.agent_roles.get(agent_name, {}).get(
            "default_model", self.system_settings.get("default_model")
        )

    def get_system_settings(self):
        """Get system-wide settings like temperature, max_tokens, etc."""
        return self.system_settings
