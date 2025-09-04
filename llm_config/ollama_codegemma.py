from langchain_ollama import OllamaLLM

def get_codegemma_model(temperature=0.7, max_tokens=512):
    return OllamaLLM(
        model="codegemma:2b",
        temperature=temperature,
        num_predict=max_tokens
    )
