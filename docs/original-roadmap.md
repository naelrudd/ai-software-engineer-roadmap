Bisa banget bro. Dan setelah aku lihat **CV-mu + listing Micro1 yang sekarang**, menurutku jangan bikin roadmap “jadi senior engineer” dulu. Kita bikin **tangga kompetensi** yang memungkinkan kamu mulai apply lebih cepat sambil terus naik level.

Micro1 sekarang punya beberapa jenis role yang membentuk tangga yang cukup jelas: dari **AI evaluation**, ke **software-engineering evaluation**, ke **coding/open-source**, lalu ke role AI engineering yang jauh lebih dalam. Contohnya ada AI Evaluation Specialist $30–90/h, Software Engineer $50–70/h, Senior/Software Engineer $50–100/h, Open Source Contributor $100–150/h, sampai AI Software Engineering Domain Expert $100–200/h. ([Micro1 Jobs][1])

Dan menariknya, CV-mu sudah punya fondasi yang lumayan besar: Python, TypeScript/JavaScript, Next.js/React, Node, Flask, REST API, database, testing, Docker/Linux, LLM, RAG, dan AI coding agents.

Jadi **kita bukan mulai dari nol.**

---

# 🧭 ROADMAP BESAR KAMU

Aku akan bikin seperti ini:

```text
LEVEL 0
Software Fundamentals
        ↓
LEVEL 1
Professional Git + Testing + Debugging
        ↓
LEVEL 2
Backend + API + Database
        ↓
LEVEL 3
CI/CD + Docker + Cloud
        ↓
LEVEL 4
AI-assisted Software Engineering
        ↓
LEVEL 5
AI Evaluation
        ↓
LEVEL 6
Coding-Agent Evaluation
        ↓
LEVEL 7
Open Source + Complex Codebase
        ↓
LEVEL 8
AI Engineering / Agent Engineering
        ↓
LEVEL 9
Micro1 High-End Roles
```

**Dan kamu tidak harus menyelesaikan Level 9 untuk mulai apply.**

---

# 🟢 LEVEL 0 — Rapikan Programming Fundamentals

### Target

Kamu harus bisa melihat kode orang lain dan berkata:

> "Oke, gue ngerti program ini melakukan apa."

Bukan cuma:

> "Kalau bikin dari awal gue bisa."

Karena pekerjaan Micro1 banyak meminta **review, debugging, code evaluation, dan memahami unfamiliar codebase**. ([Micro1 Jobs][2])

### Kuasai

**Python**

```text
functions
classes
exceptions
modules
typing
async/await
generators
file I/O
JSON
HTTP
logging
```

**JavaScript/TypeScript**

```text
async/await
Promise
closures
types
interfaces
generics
modules
error handling
```

**Data structures**

```text
Array/List
HashMap/Dictionary
Stack
Queue
Set
Tree
Graph
Heap
```

**Algorithms**

```text
sorting
searching
recursion
BFS
DFS
two pointers
sliding window
binary search
basic dynamic programming
Big-O
```

### Tools

* VS Code / Zed
* Python
* Node.js
* Git
* GitHub

### Project latihan

Jangan cuma LeetCode.

Bikin:

**`nael-algorithms`**

```text
/arrays
/strings
/hashmaps
/trees
/graphs
/sorting
/searching
```

Setiap problem:

```text
problem.md
solution.py
test_solution.py
README.md
```

Ini sekaligus mulai membangun GitHub portfolio.

---

# 🟢 LEVEL 1 — Git + Debugging + Testing

**Ini sangat penting.**

Beberapa role Micro1 secara eksplisit meminta Git/GitHub workflow, PR, code review, branching, diff analysis, CI logs, dan automated testing. ([Micro1 Jobs][3])

Kamu harus nyaman dengan:

```bash
git clone
git branch
git checkout
git switch
git add
git commit
git diff
git log
git reset
git revert
git stash
git merge
git rebase
git cherry-pick
```

Kemudian GitHub:

```text
Pull Request
Issues
Code Review
Actions
Releases
Tags
```

### Testing

Python:

```text
pytest
fixtures
mock
unit test
integration test
```

JS:

```text
Vitest
Jest
```

Kamu sudah punya Jest/Vitest/Pytest di CV.

Sekarang targetnya bukan sekadar **"pernah pakai"**.

Target:

> **Bisa membuat test yang sengaja menangkap bug.**

---

# 🟢 LEVEL 2 — Backend Engineering

Ini bakal sangat membantu kamu menuju Senior Software Engineer listing.

Micro1 meminta kemampuan backend, API, debugging, automated testing dan scalable services. ([Micro1 Jobs][4])

Kamu sudah punya:

```text
Node
Flask
Laravel
REST API
MySQL
PostgreSQL
Convex
```



Sekarang perdalam **satu stack utama**.

Aku sarankan:

# Python + FastAPI

Kenapa?

Karena nanti membuka jalan ke:

```text
Python
        ↓
FastAPI
        ↓
AI APIs
        ↓
LLM
        ↓
RAG
        ↓
Agents
        ↓
AI Engineering
```

Pelajari:

```text
HTTP
REST
CRUD
Authentication
JWT
OAuth basics
Webhooks
Pagination
Rate limiting
Caching
Logging
Error handling
Background jobs
SQL
Transactions
Indexes
```

---

# 🟢 LEVEL 3 — Docker + CI/CD + Cloud

Ini salah satu gap yang menurutku perlu kamu naikkan.

Ada listing Micro1 yang secara eksplisit meminta:

> CI/CD + Python/Bash + REST API + OAuth + webhook + GitHub workflows. ([Micro1 Jobs][3])

### Kuasai Docker

Minimal:

```text
Dockerfile
docker build
docker run
docker compose
volumes
networks
environment variables
healthcheck
```

Lalu:

# GitHub Actions

Bikin workflow:

```yaml
push
   ↓
GitHub Actions
   ↓
install dependencies
   ↓
run tests
   ↓
lint
   ↓
build
   ↓
deploy
```

### Project

Ambil salah satu project-mu.

Misalnya **KanvasHub**.

Jadikan:

```text
PR
 ↓
GitHub Actions
 ↓
pytest / Vitest
 ↓
build
 ↓
deployment
```

Jadi kamu bisa mengatakan secara konkret:

> "I built and maintained CI/CD workflows..."

bukan cuma mencantumkan GitHub Actions sebagai skill.

---

# 🟢 LEVEL 4 — AI-Assisted Software Engineering

Ini justru **senjata utama kamu**.

CV-mu sudah mencantumkan:

> Claude Code, Kiro, OpenCode



Micro1 juga secara eksplisit mencari orang yang terbiasa menggunakan AI assistants/agents dalam workflow developer. ([Micro1 Jobs][3])

Sekarang jangan hanya:

> "AI bantu coding."

Pelajari bagaimana **mengontrol AI coding agent**.

### Kuasai:

```text
context engineering
prompt engineering
agent instructions
repository context
tool calling
MCP
subagents
verification
test-driven development
code review
diff review
```

Workflow ideal:

```text
AI Agent
   ↓
Analyze repo
   ↓
Plan
   ↓
Implement
   ↓
Run tests
   ↓
Find failure
   ↓
Fix
   ↓
Run tests again
   ↓
Review diff
   ↓
Human approval
```

---

# 🟢 LEVEL 5 — AI Evaluation

**Nah ini yang menurutku bisa jadi entry point kamu.**

Ada role Micro1 yang secara khusus berfokus pada mengevaluasi output AI: membandingkan jawaban, memberi penilaian, menulis rationale, dan menemukan factual/technical errors. ([Micro1 Jobs][5])

Dan role AI Evaluation Specialist juga secara eksplisit meminta:

```text
AI Agents
Rubric-Based Evaluation
Quality Assurance
Process Improvement
```

([Micro1 Jobs][1])

### Yang harus kamu pelajari

Bukan "cara pakai ChatGPT".

Tapi:

### 1. Rubric

Contoh:

```text
Correctness       40%
Completeness      20%
Code quality      15%
Security          10%
Performance       10%
Communication      5%
```

### 2. Pairwise evaluation

```text
Answer A
vs
Answer B
```

Kemudian:

```text
Which is better?
Why?
What specific error exists?
```

### 3. Hallucination detection

AI bilang:

> "React automatically caches this API request."

Kamu harus bisa bilang:

> "Incorrect. Here's why..."

### 4. Code evaluation

AI memberikan:

```python
def get_user(id):
    ...
```

Kamu cek:

```text
correct?
edge cases?
security?
performance?
maintainability?
tests?
```

---

# 🟢 LEVEL 6 — Coding-Agent Evaluation

Ini level yang menurutku **paling cocok dengan arahmu**.

Micro1 punya role yang meminta orang membuat coding tasks untuk AI, membuat reference solutions, debugging, serta membuat deterministic verifiers. ([Micro1 Jobs][4])

Misalnya:

### Task

> Fix authentication bug in this repository.

AI mengerjakan.

Kamu:

```text
1. Review patch
2. Run tests
3. Find hidden bug
4. Create test
5. Verify solution
```

### Yang harus dipelajari

```text
pytest
test fixtures
integration tests
mocking
property-based testing
regression tests
edge cases
deterministic verification
```

---

# 🟡 LEVEL 7 — Open Source

Ini yang bakal menaikkan kredibilitasmu secara signifikan.

Micro1 punya role Open Source Contributor yang secara eksplisit mencari **meaningful ownership/contributions**, bukan sekadar typo/documentation edits. Mereka ingin kandidat mampu menjelaskan repository, PR, issues, dan code yang benar-benar dibuat sendiri. ([Micro1 Jobs][6])

Jadi kita bikin target:

### 1 repository milikmu

Misalnya:

```text
github.com/naelrudd/ai-eval-kit
```

Isinya:

```text
AI coding evaluation toolkit
```

Kemudian:

```text
Issues
PRs
Tests
CI
Documentation
Releases
```

Lalu mulai contribute ke open-source lain.

Tidak perlu langsung React/Linux.

Mulai dari project Python/TypeScript yang ukurannya masih bisa kamu pahami.

---

# 🟡 LEVEL 8 — Go

Ini khusus untuk membuka pintu role:

**Software Engineer — Go/Python/TS $100–130/h**

Listing tersebut secara eksplisit mengatakan **Go adalah primary language**, Python dan TypeScript secondary. ([Micro1 Jobs][7])

Jadi setelah fondasi kuat:

```text
Go syntax
 ↓
interfaces
 ↓
struct
 ↓
goroutines
 ↓
channels
 ↓
HTTP server
 ↓
REST API
 ↓
PostgreSQL
 ↓
testing
 ↓
Docker
```

Project:

> **Go REST API + PostgreSQL + Docker + GitHub Actions**

---

# 🔴 LEVEL 9 — AI Engineering

Ini sudah menuju role core-team.

Micro1 sekarang bahkan punya:

**Forward Deployed Engineer**

yang meminta Python, LLM systems, ML infrastructure, RAG/AI automation, multi-agent systems, tool-using agents, evaluation harnesses, dan production deployment. ([Micro1 Jobs][8])

Dan ada AI/ML Engineer yang meminta:

```text
Python
LLMs
RAG
AWS
```

([Micro1 Jobs][9])

### Skill tree

```text
Python
 │
 ├── FastAPI
 │
 ├── Async
 │
 └── AI
       │
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

---

# 🧠 Tapi jangan belajar semuanya sekaligus

Ini bagian yang **paling penting**.

Kalau kamu bilang:

> "Aku mau belajar Python + Java + Rust + C++ + Go + AWS + Kubernetes + RAG + Agents..."

**Jangan.**

Kamu bakal stuck 2 bulan di tutorial.

Aku justru akan membuat:

# `Nael → Micro1 Skill Ladder`

### Fase 1 — 2–3 minggu

```text
Git
Python
Testing
Debugging
REST API
```

**Apply:**

🟢 AI Evaluation
🟢 Software Engineer evaluation

---

### Fase 2 — 3–5 minggu

```text
FastAPI
PostgreSQL
Docker
GitHub Actions
OAuth
Webhooks
```

**Apply:**

🟢 Software Engineer $50–70
🟡 Full Stack $50–100

---

### Fase 3 — 4–6 minggu

```text
AI evaluation
rubrics
code evaluation
coding agents
test environments
deterministic verification
```

**Apply:**

🟢 AI/software evaluation
🟡 Senior Software Engineer

---

### Fase 4 — 1–2 bulan

```text
Open Source
Algorithms
Data Structures
Code review
Large codebase
Go
```

**Apply:**

🟢 Open Source Contributor
🟢 Software Engineer $50–100
🟡 Go/Python/TS $100–130

---

### Fase 5 — lanjut

```text
RAG
Agents
MCP
Evaluation harness
AWS
ML infrastructure
Multi-agent systems
```

**Target jangka panjang:**

```text
AI Software Engineering Expert
Forward Deployed Engineer
AI/ML Engineer
Coding Research
```

---

# 🛠️ Tools yang aku rekomendasikan buat kamu

Karena kamu sudah menggunakan Linux/Fedora, GitHub, OpenCode, dll., aku justru **tidak ingin kamu menambah 20 aplikasi baru**.

Pakai stack ini:

### Coding

**VS Code / Zed**

↓

### AI coding

**OpenCode**

**Claude Code**

↓

### Version control

**Git + GitHub**

↓

### Backend

**Python + FastAPI**

↓

### Testing

**Pytest**

↓

### Database

**PostgreSQL**

↓

### Container

**Docker**

↓

### CI/CD

**GitHub Actions**

↓

### AI

**OpenAI / Anthropic / OpenRouter**

↓

### Agent

**MCP**

↓

### Deployment

**Vercel + Railway/Render/AWS**

---

# 🤖 Dan AI-nya jangan cuma jadi guru

Ini bagian yang menurutku bakal cocok banget buatmu.

Bikin AI menjadi:

### Teacher

> "Jelaskan kenapa test ini gagal."

### Pair programmer

> "Jangan langsung kasih solusi. Beri aku hint."

### Code reviewer

> "Review PR ini seperti senior engineer."

### Interviewer

> "Interview aku untuk Micro1 Software Engineer."

### Evaluator

> "Berikan dua solusi AI. Aku akan menentukan mana yang lebih baik."

### Debugging partner

> "Aku akan memperbaiki bug ini sendiri. Jangan kasih jawaban langsung."

---

# 🔥 Bahkan kita bisa bikin "Micro1 Training Lab" sendiri

Ini menurutku **project paling worth it** buat kamu.

Repository:

```text
naelrudd/micro1-engineering-lab
```

Struktur:

```text
micro1-engineering-lab/

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

Setiap level punya:

```text
📚 Learn
🧪 Exercise
🐛 Bug
🤖 AI Challenge
📝 Evaluation
🏆 Final Task
```

Contohnya:

```text
AI diberikan repository rusak.

AI harus:
→ menemukan bug
→ membuat patch
→ menulis test
→ menjalankan test
→ memperbaiki
```

**Kamu kemudian mengevaluasi AI-nya.**

Itu literally melatih skill yang diminta beberapa listing Micro1. ([Micro1 Jobs][4])

---

# 📌 Prioritas skill kamu sekarang

Kalau aku bikin ranking berdasarkan **gap CV-mu + relevansi listing yang kita lihat**, urutannya:

```text
████████████████████  Git + GitHub
███████████████████   Testing
███████████████████   Debugging
██████████████████    Python
██████████████████    REST API
█████████████████     Backend
█████████████████     AI evaluation
████████████████      CI/CD
███████████████       Docker
███████████████       Code review
██████████████        Algorithms
██████████████        AI agents
████████████          Open Source
███████████           Go
██████████            AWS
████████              Kubernetes
████████              ML infrastructure
```

**Jangan ke AWS/Kubernetes dulu.**

---

## 🎯 Dan strategi apply-nya

Yang paling aku suka dari rencana kamu adalah:

> **"apply sambil belajar."**

Itu justru bagus.

Jangan tunggu sampai merasa:

> "Aku sudah siap."

Karena requirement Micro1 banyak yang ditulis untuk expert/senior. Bahkan role Open Source mereka meminta meaningful open-source contribution dan kemampuan mengerjakan unfamiliar codebase. ([Micro1 Jobs][6])

Lebih baik:

```text
BELAJAR
   ↓
BUILD
   ↓
APPLY
   ↓
INTERVIEW
   ↓
GAGAL / LOLOS
   ↓
DAPAT FEEDBACK
   ↓
BELAJAR LAGI
   ↓
APPLY ROLE LEBIH TINGGI
```

Dan **kalau diterima di role yang lebih kecil, kerja itu sendiri menjadi bagian dari learning path**.

---

### Satu catatan penting

Untuk **AI Evaluation Specialist** yang sekarang muncul, lokasi yang dicantumkan Micro1 adalah **US, Canada, UK, Ireland, Australia, dan New Zealand**, jadi jangan otomatis menganggap role itu bisa kamu ambil dari Indonesia. ([Micro1 Jobs][1])

Sedangkan beberapa role engineering lain mencantumkan **Global/Remote**, jadi itu yang lebih relevan untuk kamu dari Indonesia. ([Micro1 Jobs][10])

---

Kalau aku yang nemenin kamu, aku bakal bikin ini jadi **program belajar 12 minggu yang benar-benar operasional**: **minggu 1 apa yang dipelajari → materi gratisnya apa → project apa → challenge apa → kapan mulai apply Micro1 → kapan simulasi interview → checklist "lulus level"**. Jadi bukan roadmap doang, tapi kayak **kurikulum training pribadi Nael menuju AI Software Engineer**.

[1]: https://jobs.micro1.ai/post/bd8205f4-5715-451e-91fa-d42bfd2b41f0?utm_source=chatgpt.com "AI Evaluation Specialist | Apply on Job"
[2]: https://jobs.micro1.ai/post/5c9777fe-afb2-40b1-abbb-31cee8a8d4b6?utm_source=chatgpt.com "Software Engineer - Open Source Contributions | Apply on Job"
[3]: https://jobs.micro1.ai/post/fa3908ed-a728-492b-a597-83c0adaa5026?utm_source=chatgpt.com "Software Engineer | Apply on Job"
[4]: https://jobs.micro1.ai/post/9b3377c5-01da-40d7-9304-39cc8cd20932?utm_source=chatgpt.com "Senior Software Engineer | Apply on Job"
[5]: https://jobs.micro1.ai/post/1d2ce229-22bc-4436-975a-cea4bdb39869?utm_source=chatgpt.com "Software Engineer | Apply on Job"
[6]: https://jobs.micro1.ai/post/18a809aa-0b7f-4523-ac0e-508c9f0f6f66?utm_source=chatgpt.com "Open Source Contributor (GitHub) | Apply on Job"
[7]: https://jobs.micro1.ai/post/66b20ba1-3666-49ad-9d4c-6c390b438c4e?referralCode=600e822a-da05-481f-8e92-46277b1048e2&utm_source=chatgpt.com "Software Engineer (Go, Python, TS) | Apply on Job"
[8]: https://jobs.micro1.ai/post/44668e06-3191-4b5f-a41c-b19e05f46eb7?utm_source=chatgpt.com "Forward Deployed Engineer | Apply on Job"
[9]: https://jobs.micro1.ai/post/d1faea65-4f6a-4bfb-8616-fbfbdd997474?utm_source=chatgpt.com "AI/ML Engineer | Apply on Job"
[10]: https://jobs.micro1.ai/post/4010d2c5-4a3d-41fe-9e33-28bc218626e5?utm_source=chatgpt.com "Sr. Full-Stack Software Engineer | Apply on Job"
