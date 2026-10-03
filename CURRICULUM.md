# Kurikulum 12 Minggu

Rencana operasional: tiap minggu ada **target skill**, **sumber gratis**, **output nyata** (harus di-push), dan **checkpoint**.

Aturan: 1 minggu = minimal 10–15 jam fokus. Kalau minggu ini meleset, jangan lompat — geser saja, tapi jangan skip output.

---

## Fase 1 — Fondasi & Entry Point (Minggu 1–3)

Target apply di akhir fase: 🟢 **AI Evaluation** · 🟢 **Software Engineer Evaluation**

### Minggu 1 — Git + Python refresh

- **Skill:** Git workflow harian, Python idiomatik (typing, exceptions, modules).
- **Sumber:** [Pro Git](https://git-scm.com/book/en/v2) ch.1–3 · [Learn Git Branching](https://learngitbranching.js.org/) · [Python Tutorial](https://docs.python.org/3/tutorial/).
- **Output:** repo `nael-algorithms` dibuat, 10 soal Python + test, semua lewat branch → PR → merge.
- **Checkpoint:** bisa jelaskan `merge` vs `rebase` vs `cherry-pick` tanpa buka Google.

### Minggu 2 — Testing + Debugging

- **Skill:** pytest (fixtures, mock, parametrize), debugging dengan pdb & debugger.
- **Sumber:** [pytest docs](https://docs.pytest.org/en/stable/) · [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [pdb](https://docs.python.org/3/library/pdb.html).
- **Output:** 20+ test di `nael-algorithms`, minimal 3 test yang sengaja menangkap bug.
- **Checkpoint:** bisa tulis test yang **gagal** karena bug lalu memperbaikinya.

### Minggu 3 — Algorithms & Data Structures inti

- **Skill:** array, hashmap, stack, queue, tree, graph, sorting, BFS/DFS, Big-O.
- **Sumber:** [NeetCode Roadmap](https://neetcode.io/roadmap) · [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) · [CP-Algorithms](https://cp-algorithms.com/).
- **Output:** 25–40 soal terselesaikan di `nael-algorithms` (folder per topik).
- **Checkpoint:** bisa analisis kompleksitas solusi sendiri.

**▶ Apply sekarang:** AI Evaluation + Software Engineer Evaluation.

---

## Fase 2 — Backend & Delivery (Minggu 4–6)

Target apply di akhir fase: 🟢 **Software Engineer $50–70** · 🟡 **Full Stack $50–100**

### Minggu 4 — FastAPI + REST

- **Skill:** routing, pydantic, dependency injection, auth JWT, error handling.
- **Sumber:** [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) · [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP).
- **Output:** REST API `nael-api-lab` (CRUD + auth + pagination + rate limit).
- **Checkpoint:** endpoint ter-dokumentasi otomatis di `/docs`.

### Minggu 5 — SQL + PostgreSQL

- **Skill:** SELECT/JOIN, index, transaction, migrasi.
- **Sumber:** [SQLBolt](https://sqlbolt.com/) · [PG Exercises](https://pgexercises.com/) · [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) · [FastAPI + SQL](https://fastapi.tiangolo.com/tutorial/sql-databases/).
- **Output:** API minggu 4 pakai PostgreSQL, ada migrasi + index + test integrasi.
- **Checkpoint:** bisa baca `EXPLAIN ANALYZE` dan menjelaskan kenapa query lambat.

### Minggu 6 — Docker + CI/CD

- **Skill:** Dockerfile, compose, env, healthcheck; GitHub Actions (test → lint → build).
- **Sumber:** [Docker Get Started](https://docs.docker.com/get-started/) · [Docker Curriculum](https://docker-curriculum.com/) · [GitHub Actions](https://docs.github.com/en/actions) · [12-Factor App](https://12factor.net/).
- **Output:** API ter-containerisasi + workflow CI hijau (badge di README).
- **Checkpoint:** `docker compose up` jalan dari nol di mesin bersih.

**▶ Apply sekarang:** Software Engineer $50–70 + Full Stack.

---

## Fase 3 — AI Evaluation & Coding-Agent Evaluation (Minggu 7–9)

Target apply di akhir fase: 🟢 **AI/software evaluation** · 🟡 **Senior Software Engineer**

### Minggu 7 — AI-Assisted Engineering

- **Skill:** context engineering, agent instructions, MCP, tool calling, diff review.
- **Sumber:** [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) · [MCP](https://modelcontextprotocol.io/) · [OpenCode Docs](https://opencode.ai/docs) · [Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).
- **Output:** repo dengan `AGENTS.md`, workflow agent → plan → implement → test → fix.
- **Checkpoint:** bisa jelaskan kenapa agent gagal di satu task dan cara memperbaiki konteksnya.

### Minggu 8 — AI Evaluation

- **Skill:** rubrics, pairwise eval, hallucination detection, code evaluation.
- **Sumber:** [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) · [OpenAI Evals](https://github.com/openai/evals) · [promptfoo](https://github.com/promptfoo/promptfoo) · [HELM](https://crfm.stanford.edu/helm/).
- **Output:** 20 evaluasi tertulis (rubric + rationale + error spesifik) di `ai-eval-kit`.
- **Checkpoint:** bisa menemukan hallucination teknis dan menjelaskan koreksinya.

### Minggu 9 — Coding-Agent Evaluation

- **Skill:** reference solution, deterministic verifier, property-based testing, regression test.
- **Sumber:** [SWE-bench](https://www.swebench.com/) · [SWE-bench repo](https://github.com/princeton-nlp/SWE-bench) · [HumanEval](https://github.com/openai/human-eval) · [Hypothesis](https://hypothesis.readthedocs.io/).
- **Output:** 5 task "fix bug" lengkap dengan patch AI, test yang memverifikasi, dan skor.
- **Checkpoint:** verifier kamu menolak solusi yang "kelihatan benar tapi salah".

**▶ Apply sekarang:** AI/software evaluation + Senior Software Engineer.

---

## Fase 4 — Open Source, Algorithm Depth & Go (Minggu 10–12)

Target apply di akhir fase: 🟢 **Open Source Contributor** · 🟢 **SWE $50–100** · 🟡 **Go/Python/TS $100–130**

### Minggu 10 — Open Source

- **Skill:** baca codebase asing, cari issue, PR berkualitas.
- **Sumber:** [Open Source Guides](https://opensource.guide/) · [First Contributions](https://github.com/firstcontributions/first-contributions) · [Good First Issue](https://goodfirstissue.dev/) · [Up For Grabs](https://up-for-grabs.net/) · [First Timers Only](https://www.firsttimersonly.com/).
- **Output:** minimal 1 PR bermakna merged (bukan typo) + penjelasan di README.
- **Checkpoint:** bisa menjelaskan arsitektur repo itu dan perubahan yang kamu buat.

### Minggu 11 — Go

- **Skill:** syntax, struct, interface, goroutine, channel, HTTP server, testing.
- **Sumber:** [A Tour of Go](https://go.dev/tour/) · [Go by Example](https://gobyexample.com/) · [Effective Go](https://go.dev/doc/effective_go) · [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests) · [Go Roadmap](https://roadmap.sh/golang).
- **Output:** `nael-go-api` — REST API + PostgreSQL + Docker + GitHub Actions.
- **Checkpoint:** paham goroutine vs thread dan bisa menulis test table-driven.

### Minggu 12 — AI Engineering (naik level)

- **Skill:** LLM APIs, embeddings, vector DB, RAG, agents, tool use, eval harness, observability.
- **Sumber:** [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) · [RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) · [LangChain RAG](https://python.langchain.com/docs/tutorials/rag/) · [OpenAI Cookbook](https://github.com/openai/openai-cookbook) · [HF Cookbook](https://huggingface.co/learn/cookbook) · [LlamaIndex](https://docs.llamaindex.ai/).
- **Output:** prototype RAG + eval harness yang mengukur akurasi retrieval & jawaban.
- **Checkpoint:** bisa mengukur kualitas sistem AI, bukan cuma membangunnya.

**▶ Apply sekarang:** Open Source Contributor, SWE $50–100, Go/Python/TS $100–130.

---

## Setelah minggu 12

Target jangka panjang: **AI Software Engineering Expert · Forward Deployed Engineer · AI/ML Engineer · Coding Research**.

Lanjutkan dengan fokus: eval harness produksi, multi-agent systems, AWS, ML infrastructure. Lihat [`09-ai-engineering/README.md`](09-ai-engineering/README.md).
