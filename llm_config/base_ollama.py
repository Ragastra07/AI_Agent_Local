from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

# Load .env once
load_dotenv()

# Ensure the models path is set
os.environ["OLLAMA_MODELS_PATH"] = os.getenv(
    "OLLAMA_MODELS_PATH", "/home/ollama-models/.ollama/"
)

def get_ollama_model(model_name: str, temperature: float = 0.7, max_tokens: int = 512):
    """
    Generic Ollama model loader with system settings support
    """
    return Ollama(
        model=model_name,
        temperature=temperature,
        num_predict=max_tokens
    )
