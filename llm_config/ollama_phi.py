from langchain_ollama import OllamaLLM

def get_phi_model(temperature=0.7, max_tokens=512):
    return OllamaLLM("phi3", temperature, max_tokens)
