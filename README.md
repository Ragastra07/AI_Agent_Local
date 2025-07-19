# 🧠 Local AI Agent with Mistral, Phi-3, and Command-R

> Version: `v0.3.0-alpha`  
> Status: 🚧 Active Development

This project is a local-first AI agent system powered by lightweight, open-weight large language models (LLMs) such as **Mistral**, **Phi-3**, and **Command-R**. The goal is to create a privacy-respecting and efficient personal AI assistant that runs entirely on local hardware — no cloud, no tracking, and full control.

---

## ✅ Current Progress

### ✅ Storage Optimization & Model Migration (Completed)
- Ollama models (~19GB) moved from root partition (`/usr/share/ollama/.ollama`) to home partition (`/home/ollama-models/.ollama`)
- Symbolic link established to maintain Ollama compatibility
- Freed up ~18GB on root partition
- Verified that models like `mistral`, `phi3`, and `codegemma` work after migration

### ✅ Agent Framework Bootstrapped
- Using **LangChain** and **CrewAI** to create multi-agent systems
- Initial setup for task delegation: one agent generates, another validates
- Command-line interface running successfully with model switching

---

## 🧩 Architecture Overview

- **Model Backend**: [Ollama](https://ollama.com) for model loading and inference
- **LLMs Used**:  
  - `mistral:latest` (4.4GB)  
  - `phi3:latest` (2.2GB)  
  - `codegemma:2b` (1.6GB)  
  - `command-r` (next planned)
- **Agent Frameworks**:  
  - `LangChain` for chain-based reasoning and tool use  
  - `CrewAI` for multi-agent interaction and role separation  
- **Terminal Layer**: Custom Bash/CLI interface with optional TUI wrapper
- **Environment**: Ubuntu 22.04+, local disk storage with symbolic link management

---

## 🧠 Bias Mitigation Strategy

Even though I use pretrained models without retraining, bias mitigation is implemented through:

- Careful **model selection** (transparency, license, community review)
- Ethical **prompt engineering**
- **User-in-the-loop** validation before output is stored or executed
- Multi-agent checks: one agent **generates**, another **verifies** or **critiques** output to reduce hallucination and bias

---

## 📦 Versioning

- `v0.1.0-alpha` — Initial Ollama + Mistral testing  
- `v0.2.0-alpha` — Added Phi-3 and CodeGemma; disk migration complete  
- `v0.3.0-alpha` — LangChain + CrewAI agent workflows functional (current)  
- `v0.4.0-alpha` — [Planned] Add Command-R with `command-r-plus`  
- `v1.0.0` — [Future] First stable local AI agent release with web UI

---

## 📌 Future Plans

- [ ] Integrate `command-r` with tool usage (retrieval, search, terminal tools)
- [ ] Build lightweight Web UI or TUI for managing agents
- [ ] Add persistent memory and local database storage (e.g., SQLite or LiteFS)
- [ ] Offline documentation and self-debugging via natural language

---

## 🛡️ License

This project is for personal and educational use. Respect model licenses and use responsibly.

---

## 🙋‍♂️ About Me

I’m a developer passionate about building open, local-first AI systems. This project is part of my exploration in privacy-aware, customizable agents that run on personal machines — starting with terminal-first workflows.

Let’s connect on [LinkedIn](https://www.linkedin.com/in/ragastra-haryo-wijanarko-5ab75b1ba/) or feel free to contribute!

