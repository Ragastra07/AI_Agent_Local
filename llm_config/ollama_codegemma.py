from .base_ollama import get_ollama_model

def get_codegemma_model(temperature=0.7, max_tokens=512):
    return get_ollama_model("codegemma:2b", temperature, max_tokens)
