from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Ensure the models path is set
os.environ["OLLAMA_MODELS_PATH"] = os.getenv(
    "OLLAMA_MODELS_PATH", "/home/ollama-models/.ollama/"
)


def get_codegemma_model():
    model_name = os.getenv(
        "OLLAMA_CODEGEMMA_MODEL", "codegemma:2b"
    )  # Default to "codegemma:2b" if not set
    return Ollama(model=model_name)