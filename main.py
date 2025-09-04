from dotenv import load_dotenv
from utils.config_loader import ConfigLoader
from utils.config_loader import ConfigLoader
from llm_config.ollama_phi import get_phi_model
from llm_config.ollama_mistral import get_mistral_model
from llm_config.ollama_codegemma import get_codegemma_model
from agents.base_agent import BaseAgent

# Load .env file
load_dotenv()


if __name__ == "__main__":
    jati = BaseAgent("jati")
    print(jati.introduce())

    response = jati.chat("Can you show me how to list files in Linux?")
    print("Agent response:", response)