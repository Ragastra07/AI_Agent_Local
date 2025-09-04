from dotenv import load_dotenv
from utils.config_loader import ConfigLoader
from utils.config_loader import ConfigLoader
from llm_config.ollama_phi import get_phi_model
from llm_config.ollama_mistral import get_mistral_model
from llm_config.ollama_codegemma import get_codegemma_model


# Load .env file
load_dotenv()


if __name__ == "__main__":
    # 1. Load all config
    config = ConfigLoader()
    settings = config.get_system_settings()

    # 2. chose an agent and get its model
    agent_name = "jati"
    model_name = config.get_agent_model(agent_name)

    # 3. Load the appropriate model
    if model_name in ["phi", "ollama_phi"]:
        llm = get_phi_model(settings["temperature"], settings["max_tokens"])
    elif model_name in ["mistral", "ollama_mistral"]:
        llm = get_mistral_model(settings["temperature"], settings["max_tokens"])
    elif model_name in ["codegemma", "ollama_codegemma"]:
        llm = get_codegemma_model(settings["temperature"], settings["max_tokens"])
    else:
        raise ValueError(f"Unknown model: {model_name}")

    # 4. Get the agent's prompt template
    prompt = config.get_agent_prompt(agent_name)

    # 5. Test LLM
    response = llm.invoke(prompt + "\nHello, what can you do?")
    print("Response from", model_name, ":\n", response)
