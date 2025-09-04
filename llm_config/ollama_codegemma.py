from langchain_ollama import OllamaLLM

def get_codegemma_model(temperature=0.7, max_tokens=512):
    return OllamaLLM("codegemma:2b", temperature, max_tokens)
