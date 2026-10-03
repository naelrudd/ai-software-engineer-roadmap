# Level 9 — AI Engineering

> 🎯 **Target:** role core-team. Micro1 punya **Forward Deployed Engineer** yang minta Python, LLM systems, ML infrastructure, RAG/AI automation, multi-agent systems, tool-using agents, evaluation harnesses, dan production deployment. Ada juga **AI/ML Engineer** (Python, LLMs, RAG, AWS).

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

### Sumber gratis
- [Generative AI for Beginners (Microsoft)](https://github.com/microsoft/generative-ai-for-beginners) — kurikulum 21 pelajaran
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

Bikin repo **`nael-ai-lab`**:

- [ ] **LLM basics:** panggil LLM API, streaming, structured output, function/tool calling.
- [ ] **Embeddings + vector DB:** chunking, indexing, similarity search (pgvector / FAISS / Chroma).
- [ ] **RAG end-to-end:** ingest docs → retrieve → generate → cite sources.
- [ ] **Agent:** tool-using agent dengan MCP, minimal 2 tools.
- [ ] **Multi-agent:** 2 agent yang berkolaborasi (mis. planner + executor).
- [ ] **Evaluation harness:** ukur retrieval (precision/recall) + jawaban (faithfulness, relevancy).
- [ ] **Observability:** logging/tracing tiap panggilan LLM (token, latency, biaya).
- [ ] **Production:** containerize + deploy + rate limit + fallback.

---

## 🐛 Bug Hunt

Masalah RAG nyata yang wajib kamu temukan & perbaiki:
- Retrieval mengambil chunk tidak relevan → perbaiki chunking/embedding/reranking.
- Jawaban hallucinate walau konteks benar → perbaiki prompt/grounding.
- Latency tinggi → caching / batching / model lebih kecil.
- Biaya membengkak → ukur token, optimalkan prompt.

---

## 🤖 AI Challenge

Bangun **eval harness** untuk sistem RAG-mu sendiri. Buat dataset pertanyaan + jawaban acuan, ukur skor, dan tunjukkan versi mana yang lebih baik beserta alasannya. Ini yang membedakan AI Engineer biasa vs yang paham evaluasi.

---

## 📝 Evaluation

Buat `eval/` berisi:
- Dataset evaluasi (≥ 30 pertanyaan).
- Metrik: retrieval precision/recall, answer faithfulness, relevancy, latency, cost.
- Laporan perbandingan minimal 2 konfigurasi sistem.

---

## 🏆 Final Task

`nael-ai-lab` punya:
- [ ] RAG end-to-end yang bisa dijalankan
- [ ] Agent + tool calling (minimal 1 MCP tool)
- [ ] Eval harness dengan metrik terukur
- [ ] Observability (token, latency, biaya)
- [ ] Deploy + README + arsitektur diagram
- [ ] Laporan: konfigurasi mana terbaik & kenapa

---

## ✅ Checklist lulus Level 9

- [ ] Bisa membangun & mengukur sistem RAG, bukan cuma demo
- [ ] Paham tool calling & MCP dari sisi implementasi
- [ ] Paham pola agent (routing, orchestration, evaluator-optimizer)
- [ ] Bisa mengukur kualitas output AI secara objektif
- [ ] Bisa deploy sistem AI ke produksi dengan aman

---

## Target jangka panjang

```
AI Software Engineering Expert
Forward Deployed Engineer
AI/ML Engineer
Coding Research
```
