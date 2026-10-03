# Level 9 — AI Engineering

> 🎯 **Target:** core-team AI roles. Forward Deployed / AI-ML Engineer roles ask for Python, LLM systems, ML infrastructure, RAG/AI automation, multi-agent systems, tool-using agents, evaluation harnesses, and production deployment.

---

## 📚 Learn

### Skill tree
```
Python
  │
  ├── FastAPI
  ├── Async
  └── AI
        ├── LLM APIs
        ├── embeddings
        ├── vector DB
        ├── RAG
        ├── agents
        ├── tool calling
        ├── MCP
        ├── evaluation
        └── observability
```

### Free sources
- [Generative AI for Beginners (Microsoft)](https://github.com/microsoft/generative-ai-for-beginners) — 21-lesson curriculum
- [RAG from Scratch (LangChain)](https://github.com/langchain-ai/rag-from-scratch)
- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
- [[OI] Cookbook](https://github.com/openai/openai-cookbook)
- [Hugging Face Cookbook](https://huggingface.co/learn/cookbook)
- [Hugging Face Learn](https://huggingface.co/learn)
- [LlamaIndex Docs](https://docs.llamaindex.ai/)
- [Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)
- [Model Context Protocol](https://modelcontextprotocol.io/)

---

## 🧪 Exercise

Create the **`nael-ai-lab`** repo:

- [ ] **LLM basics:** call an LLM API, streaming, structured output, function/tool calling.
- [ ] **Embeddings + vector DB:** chunking, indexing, similarity search (pgvector / FAISS / Chroma).
- [ ] **RAG end-to-end:** ingest docs → retrieve → generate → cite sources.
- [ ] **Agent:** tool-using agent with MCP, at least 2 tools.
- [ ] **Multi-agent:** 2 agents collaborating (e.g. planner + executor).
- [ ] **Evaluation harness:** measure retrieval (precision/recall) + answers (faithfulness, relevancy).
- [ ] **Observability:** log/trace every LLM call (tokens, latency, cost).
- [ ] **Production:** containerize + deploy + rate limit + fallback.

---

## 🐛 Bug Hunt

Real RAG problems you must find & fix:
- Retrieval returns irrelevant chunks → fix chunking/embedding/reranking.
- Answers hallucinate even when context is correct → fix prompt/grounding.
- High latency → caching / batching / a smaller model.
- Costs ballooning → measure tokens, optimize the prompt.

---

## 🤖 AI Challenge

Build an **eval harness** for your own RAG system. Create a question set + reference answers, measure scores, and show which version is better and why. This is what separates a real AI Engineer from someone who can only demo.

---

## 📝 Evaluation

Create `eval/` containing:
- An evaluation dataset (≥ 30 questions).
- Metrics: retrieval precision/recall, answer faithfulness, relevancy, latency, cost.
- A comparison report of at least 2 system configurations.

---

## 🏆 Final Task

`nael-ai-lab` has:
- [ ] A runnable end-to-end RAG
- [ ] An agent + tool calling (at least 1 MCP tool)
- [ ] An eval harness with measurable metrics
- [ ] Observability (tokens, latency, cost)
- [ ] Deploy + README + architecture diagram
- [ ] A report: which configuration is best & why

---

## ✅ Level 9 pass checklist

- [ ] Can build & measure a RAG system, not just demo it
- [ ] Understand tool calling & MCP from the implementation side
- [ ] Understand agent patterns (routing, orchestration, evaluator-optimizer)
- [ ] Can objectively measure AI output quality
- [ ] Can deploy an AI system to production safely

---

## Long-term targets

```
AI Software Engineering Expert
Forward Deployed Engineer
AI/ML Engineer
Coding Research
```
