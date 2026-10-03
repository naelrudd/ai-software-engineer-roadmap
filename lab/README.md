# Lab — nael-algorithms

The hands-on **learning + practice lab** for the [AI Software Engineer Roadmap](../README.md): Python, algorithms, data structures, testing, and debugging.

This is not a LeetCode dump. It's a self-paced course: each **module** teaches a concept with real explanation and pitfalls, each **workshop** is a guided hands-on session, and each **exercise** is a problem you solve with tests.

The goal is simple: get comfortable reading, writing, testing, and debugging code you didn't write — the core skill for any software engineering or AI-evaluation role.

> Run all commands from inside this `lab/` directory.

---

## How this repo is organized

```
nael-algorithms/
├── README.md                 # you are here
├── SYLLABUS.md               # the full module + workshop plan
├── CONTRIBUTING.md           # how to work in this repo (git workflow)
├── Makefile                  # common commands (make test, make fmt)
├── pyproject.toml            # tooling config (pytest, ruff)
├── docs/
│   ├── how-to-use.md         # how to study here
│   └── git-workflow.md       # branch → PR → review → merge
├── templates/
│   └── problem/              # template for a new exercise
├── modules/                  # 📚 lessons (theory + exercises)
├── workshops/                # 🧪 guided hands-on sessions
└── exercises/                # your solved problems (with tests)
```

---

## The learning loop

For every module:

```
1. Read the module README (concepts + pitfalls)
2. Do the workshop for that module
3. Solve the exercises (write code + tests yourself)
4. Commit via a branch + PR
5. Move to the next module
```

Never skip the tests. A solution without a test is not done.

---

## Quick start

```bash
# 1. (optional) create a virtualenv
python -m venv .venv && source .venv/bin/activate

# 2. install dev tools
pip install -e ".[dev]"

# 3. run the test suite
make test          # or: pytest -q

# 4. start with the first module
open modules/00-python-refresh/README.md
```

> No `make`? Every command is just a thin wrapper — see the `Makefile`, or run the `pytest` command directly.

---

## Where to start

1. Read [`SYLLABUS.md`](SYLLABUS.md) — the whole plan, in order.
2. Read [`docs/how-to-use.md`](docs/how-to-use.md) — the study method.
3. Begin at [`modules/00-python-refresh`](modules/00-python-refresh/README.md).
4. Do [`workshops/01-git-and-repo-setup`](workshops/01-git-and-repo-setup/README.md) first — it sets up your workflow.

---

## Progress

Track yourself in [`SYLLABUS.md`](SYLLABUS.md). Mark a module done only when its exercises pass with tests.
