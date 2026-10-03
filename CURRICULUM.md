# 12-Week Curriculum

The operational plan: each week has a **skill target**, **free sources**, a **real output** (must be pushed), and a **checkpoint**.

Rule: 1 week = at least 10–15 focused hours. If a week slips, don't skip ahead — just shift it, but never skip the output.

Weeks 1–6 build the **universal core**. Weeks 7–12 **narrow into a specialization** (AI evaluation, coding-agent evaluation, open source/backend, or AI engineering). You can stop at any point and still be hireable — each phase ends with an application checkpoint.

---

## Phase 1 — Foundations (Weeks 1–3)

By the end of this phase you're ready to apply for: **junior/mid software engineering and AI evaluation roles.**

### Week 1 — Git + Python refresh

- **Skill:** daily Git workflow, idiomatic Python (typing, exceptions, modules).
- **Sources:** [Pro Git](https://git-scm.com/book/en/v2) ch.1–3 · [Learn Git Branching](https://learngitbranching.js.org/) · [Python Tutorial](https://docs.python.org/3/tutorial/).
- **Output:** `nael-algorithms` repo created, 10 Python problems + tests, all via branch → PR → merge.
- **Checkpoint:** explain `merge` vs `rebase` vs `cherry-pick` without opening Google.

### Week 2 — Testing + Debugging

- **Skill:** pytest (fixtures, mock, parametrize), debugging with pdb & a debugger.
- **Sources:** [pytest docs](https://docs.pytest.org/en/stable/) · [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [pdb](https://docs.python.org/3/library/pdb.html).
- **Output:** 20+ tests in `nael-algorithms`, at least 3 tests that deliberately catch bugs.
- **Checkpoint:** write a test that **fails** because of a bug, then fix it.

### Week 3 — Core Algorithms & Data Structures

- **Skill:** array, hashmap, stack, queue, tree, graph, sorting, BFS/DFS, Big-O.
- **Sources:** [NeetCode Roadmap](https://neetcode.io/roadmap) · [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) · [CP-Algorithms](https://cp-algorithms.com/).
- **Output:** 25–40 problems solved in `nael-algorithms` (folder per topic).
- **Checkpoint:** analyze the complexity of your own solutions.

**▶ Apply now:** junior/mid SWE + AI evaluation.

---

## Phase 2 — Backend & Delivery (Weeks 4–6)

By the end of this phase you're ready for: **software engineer / full-stack roles.**

### Week 4 — FastAPI + REST

- **Skill:** routing, pydantic, dependency injection, JWT auth, error handling.
- **Sources:** [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) · [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP).
- **Output:** REST API `nael-api-lab` (CRUD + auth + pagination + rate limiting).
- **Checkpoint:** endpoints auto-documented at `/docs`.

### Week 5 — SQL + PostgreSQL

- **Skill:** SELECT/JOIN, indexes, transactions, migrations.
- **Sources:** [SQLBolt](https://sqlbolt.com/) · [PG Exercises](https://pgexercises.com/) · [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) · [FastAPI + SQL](https://fastapi.tiangolo.com/tutorial/sql-databases/).
- **Output:** Week 4 API on PostgreSQL, with migrations + indexes + integration tests.
- **Checkpoint:** read `EXPLAIN ANALYZE` and explain why a query is slow.

### Week 6 — Docker + CI/CD

- **Skill:** Dockerfile, compose, env, healthcheck; GitHub Actions (test → lint → build).
- **Sources:** [Docker Get Started](https://docs.docker.com/get-started/) · [Docker Curriculum](https://docker-curriculum.com/) · [GitHub Actions](https://docs.github.com/en/actions) · [12-Factor App](https://12factor.net/).
- **Output:** containerized API + green CI workflow (badge in README).
- **Checkpoint:** `docker compose up` works from scratch on a clean machine.

**▶ Apply now:** software engineer / full-stack.

---

## Phase 3 — AI-Assisted Engineering & Evaluation (Weeks 7–9)

By the end of this phase you're ready for: **AI evaluation, coding-agent evaluation, senior SWE.**

### Week 7 — AI-Assisted Engineering

- **Skill:** context engineering, agent instructions, MCP, tool calling, diff review.
- **Sources:** [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) · [MCP](https://modelcontextprotocol.io/) · [OpenCode Docs](https://opencode.ai/docs) · [Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).
- **Output:** a repo with `AGENTS.md`, agent workflow → plan → implement → test → fix.
- **Checkpoint:** explain why an agent failed at one task and how to fix its context.

### Week 8 — AI Evaluation

- **Skill:** rubrics, pairwise eval, hallucination detection, code evaluation.
- **Sources:** [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) · [[OI] Evals](https://github.com/openai/evals) · [promptfoo](https://github.com/promptfoo/promptfoo) · [HELM](https://crfm.stanford.edu/helm/).
- **Output:** 20 written evaluations (rubric + rationale + specific error) in `ai-eval-kit`.
- **Checkpoint:** detect a technical hallucination and explain the correction.

### Week 9 — Coding-Agent Evaluation

- **Skill:** reference solution, deterministic verifier, property-based testing, regression tests.
- **Sources:** [SWE-bench](https://www.swebench.com/) · [SWE-bench repo](https://github.com/princeton-nlp/SWE-bench) · [HumanEval](https://github.com/openai/human-eval) · [Hypothesis](https://hypothesis.readthedocs.io/).
- **Output:** 5 "fix the bug" tasks, each with the AI's patch, a verifying test, and a score.
- **Checkpoint:** your verifier rejects solutions that "look right but aren't".

**▶ Apply now:** AI evaluation + coding-agent evaluation + senior SWE.

---

## Phase 4 — Specialization Depth (Weeks 10–12)

Pick the branch that matches your target. All three lead to **senior / specialized roles.**

### Week 10 — Open Source

- **Skill:** read unfamiliar codebases, find issues, high-quality PRs.
- **Sources:** [Open Source Guides](https://opensource.guide/) · [First Contributions](https://github.com/firstcontributions/first-contributions) · [Good First Issue](https://goodfirstissue.dev/) · [Up For Grabs](https://up-for-grabs.net/) · [First Timers Only](https://www.firsttimersonly.com/).
- **Output:** at least 1 meaningful merged PR (not a typo fix) + write-up in the README.
- **Checkpoint:** explain that repo's architecture and the change you made.

### Week 11 — Go (or deepen another language)

- **Skill:** syntax, struct, interface, goroutine, channel, HTTP server, testing.
- **Sources:** [A Tour of Go](https://go.dev/tour/) · [Go by Example](https://gobyexample.com/) · [Effective Go](https://go.dev/doc/effective_go) · [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests) · [Go Roadmap](https://roadmap.sh/golang).
- **Output:** `nael-go-api` — REST API + PostgreSQL + Docker + GitHub Actions.
- **Checkpoint:** understand goroutine vs thread and write table-driven tests.
- *(Not into Go? Deepen TypeScript/Node or Rust instead — same structure.)*

### Week 12 — AI Engineering

- **Skill:** LLM APIs, embeddings, vector DB, RAG, agents, tool use, eval harness, observability.
- **Sources:** [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) · [RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch) · [LangChain RAG](https://python.langchain.com/docs/tutorials/rag/) · [[OI] Cookbook](https://github.com/openai/openai-cookbook) · [HF Cookbook](https://huggingface.co/learn/cookbook) · [LlamaIndex](https://docs.llamaindex.ai/).
- **Output:** a RAG prototype + an eval harness measuring retrieval and answer quality.
- **Checkpoint:** measure the quality of an AI system, not just build one.

**▶ Apply now:** open source contributor, senior SWE, AI/LLM engineer.

---

## After week 12

Long-term targets: **AI Software Engineering Expert · Forward Deployed Engineer · AI/ML Engineer · Coding Research**.

Keep going with a focus on: production eval harnesses, multi-agent systems, cloud infrastructure, ML infrastructure. See [`09-ai-engineering/README.md`](09-ai-engineering/README.md).
