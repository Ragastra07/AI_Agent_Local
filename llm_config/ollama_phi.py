from langchain_ollama import OllamaLLM

def get_phi_model(temperature=0.7, max_tokens=512):
    return OllamaLLM(
        model="phi3",
        temperature=temperature,
        num_predict=max_tokens
    )
