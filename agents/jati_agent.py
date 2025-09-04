from llm_config.ollama_codegemma import query_codegemma

class JatiAgent:
    def __init__(self, use_context=False):
        self.use_context = use_context

    def handle_request(self, prompt: str, context: str = ""):
        """
        Kirim permintaan ke model Ollama (CodeGemma) dengan optional context
        """
        if self.use_context and context:
            full_prompt = f"{context}\n\n{prompt}"
        else:
            full_prompt = prompt

        response = query_codegemma(full_prompt)
        return response
