# Projects — Concrete Portfolio

Every level produces a repo. Together they become your portfolio when you apply.

| # | Repo | Level | Description | Status |
|---|------|-------|-------------|--------|
| 1 | `nael-algorithms` | 0–1 | DSA + Python, 25–40 problems, each with tests + Big-O analysis | `[ ]` |
| 2 | `nael-api-lab` | 2–3 | REST API: FastAPI + PostgreSQL + JWT + Docker + CI/CD | `[ ]` |
| 3 | `agent-workflow-lab` | 4 | AI agent workflow + `AGENTS.md` + context engineering | `[ ]` |
| 4 | `ai-eval-kit` | 5–7 | AI coding evaluation toolkit (rubrics, pairwise, hallucination) | `[ ]` |
| 5 | `coding-agent-eval` | 6 | Coding tasks + reference solutions + deterministic verifiers + harness | `[ ]` |
| 6 | `nael-go-api` | 8 | Go REST API + PostgreSQL + Docker + CI | `[ ]` |
| 7 | `nael-ai-lab` | 9 | RAG + agents + eval harness + observability + deploy | `[ ]` |
| 8 | `engineering-lab` | all | Combined practice lab (optional, see below) | `[ ]` |

---

## Rules for every repo

Every portfolio repo **must** have:

- [ ] A clear README: what it is, why it exists, how to run it, its architecture.
- [ ] Passing tests.
- [ ] Green CI (badge).
- [ ] Clean commit history (small commits, clear messages).
- [ ] At least 1 PR you reviewed/merged yourself.
- [ ] No secrets in the code.

---

## (Optional) `engineering-lab`

A combined lab of all levels in one repo:

```
engineering-lab/
├── 01-python/
├── 02-algorithms/
├── 03-git/
├── 04-debugging/
├── 05-testing/
├── 06-rest-api/
├── 07-docker/
├── 08-ci-cd/
├── 09-ai-evaluation/
├── 10-agent-evaluation/
├── 11-open-source/
└── README.md
```

Each level contains:

```
📚 Learn
🧪 Exercise
🐛 Bug
🤖 AI Challenge
📝 Evaluation
🏆 Final Task
```

Example challenge flow:

```
An AI is given a broken repository.
The AI must: find the bug → write a patch → write tests
            → run tests → fix
Then you evaluate the AI's work.
```

That trains the exact skill several evaluation roles ask for.

---

## Portfolio checklist before applying

- [ ] Every repo has a quality README
- [ ] Every repo has green CI
- [ ] GitHub profile tidied (bio, pinned repos)
- [ ] At least 1 merged open-source PR (Level 7)
- [ ] Can explain each repo in 2 minutes
