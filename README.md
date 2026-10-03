# AI Software Engineer Roadmap

A universal, 12-week learning roadmap from **solid software fundamentals** to **AI Software Engineer / AI Evaluation Engineer** — then narrowing into whichever specialization you choose.

It's built to work for any self-taught developer with some web/backend experience, regardless of which company or platform you're targeting. Micro1 roles are used as one concrete reference point (they publish public listings with clear skill requirements), but the skills themselves are universal and portable.

The principle: **don't learn everything at once.** Level up, apply, get feedback, level up again.

> The original analysis that seeded this repo is in [`docs/original-roadmap.md`](docs/original-roadmap.md).

---

## How to use this repo

1. Open [`CURRICULUM.md`](CURRICULUM.md) — the operational 12-week plan (week 1–12, target per week).
2. Work through the levels in order, starting at [`00-fundamentals/`](00-fundamentals/README.md).
3. Mark progress in [`PROGRESS.md`](PROGRESS.md) after each task.
4. All free resources are collected in [`RESOURCES.md`](RESOURCES.md).
5. Concrete practice projects live in [`projects/`](projects/README.md).
6. **Do the hands-on work in [`lab/`](lab/README.md)** — 15 modules + 8 workshops + exercises with tests and CI. Start at [`lab/SYLLABUS.md`](lab/SYLLABUS.md).

> **Docs vs Lab:** the level folders (`00-fundamentals/` … `09-ai-engineering/`) are the *plan* — what to learn and why. [`lab/`](lab/README.md) is the *practice* — actual lessons, workshops, and code you write.

**Ground rule:** every level follows the same format — 🎯 Target · 📚 Learn · 🧪 Exercise · 🐛 Bug Hunt · 🤖 AI Challenge · 📝 Evaluation · 🏆 Final Task · ✅ Pass checklist.

---

## The shape: universal core → specialization

```
        UNIVERSAL CORE (Levels 0–4)
   fundamentals · git · testing · backend · delivery · AI-assisted engineering
                        │
        ┌───────────────┼────────────────┬───────────────────┐
        ▼               ▼                ▼                   ▼
  AI EVALUATION   CODING-AGENT      OPEN SOURCE /       AI ENGINEERING
   (Level 5)      EVALUATION         BACKEND / GO        (Level 9)
                   (Level 6)          (Levels 7–8)        LLM · RAG · agents
```

Levels 0–4 are universal: they make you a competent, hireable software engineer and an effective AI-assisted developer. Levels 5–9 are where you narrow toward a specialization. You don't have to do all of them — pick the branch that matches the role you want.

---

## Level map

| Level | Folder | Focus | Core / Specialization |
|-------|--------|-------|-----------------------|
| 0 | [00-fundamentals](00-fundamentals/README.md) | Programming fundamentals, DSA | Universal core |
| 1 | [01-git-testing-debugging](01-git-testing-debugging/README.md) | Git, testing, debugging | Universal core |
| 2 | [02-backend-api-database](02-backend-api-database/README.md) | FastAPI, SQL, PostgreSQL | Universal core |
| 3 | [03-docker-ci-cd-cloud](03-docker-ci-cd-cloud/README.md) | Docker, GitHub Actions | Universal core |
| 4 | [04-ai-assisted-engineering](04-ai-assisted-engineering/README.md) | AI coding agents, MCP, context engineering | Universal core |
| 5 | [05-ai-evaluation](05-ai-evaluation/README.md) | Rubrics, pairwise eval, hallucination | Specialization |
| 6 | [06-coding-agent-evaluation](06-coding-agent-evaluation/README.md) | SWE-bench style, deterministic verifiers | Specialization |
| 7 | [07-open-source](07-open-source/README.md) | Meaningful open-source contribution | Specialization |
| 8 | [08-go](08-go/README.md) | Go + REST API + PostgreSQL | Specialization |
| 9 | [09-ai-engineering](09-ai-engineering/README.md) | LLM, RAG, agents, MCP, eval harness | Specialization |

---

## Level-up rules (definition of done)

A level **passes** only when all of these hold:

- [ ] Every topic under 📚 Learn is covered (at least 1 primary source + 1 hands-on).
- [ ] Every 🧪 Exercise is done and committed to GitHub.
- [ ] At least 1 🐛 Bug Hunt succeeds (find a real bug + write a regression test).
- [ ] The 🤖 AI Challenge is done — *you* evaluate the AI, not the reverse.
- [ ] The 🏆 Final Task is complete and pushed.
- [ ] `PROGRESS.md` is updated.

---

## Application strategy (read this before worrying you're "not ready")

```
LEARN → BUILD → APPLY → INTERVIEW → FAIL/PASS
   → GET FEEDBACK → LEARN AGAIN → APPLY FOR A HIGHER ROLE
```

- Don't wait until you *feel* ready. Job requirements are often written for more senior people than the role really needs.
- Remote/global roles are the most portable; local roles have their own market.
- If you land a smaller role, that job itself becomes part of the learning path.
- When a listing names a location restriction, read it carefully before applying — some roles are region-locked.

---

## Tools (don't add 20 new apps)

```
Coding         : VS Code / Zed
AI coding      : OpenCode, [CC]
Version control: Git + GitHub
Backend        : Python + FastAPI
Testing        : Pytest, Vitest/Jest
Database       : PostgreSQL
Container      : Docker
CI/CD          : GitHub Actions
AI             : [OI] / Anthropic / OpenRouter
Agent          : MCP
Deploy         : Vercel + Railway/Render/AWS
```

---

## Progress at a glance

See [`PROGRESS.md`](PROGRESS.md) for the full checklist and per-level status.
