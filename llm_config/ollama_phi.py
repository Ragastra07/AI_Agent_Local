from .base_ollama import get_ollama_model

def get_phi_model(temperature=0.7, max_tokens=512):
    return get_ollama_model("phi3", temperature, max_tokens)
