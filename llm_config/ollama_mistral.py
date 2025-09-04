from langchain_ollama import OllamaLLM

def get_mistral_model(temperature=0.7, max_tokens=512):
    return OllamaLLM(
        model="mistral",
        temperature=temperature,
        num_predict=max_tokens
    )
