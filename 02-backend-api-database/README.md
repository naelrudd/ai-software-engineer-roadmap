# Level 2 — Backend + API + Database

> 🎯 **Target:** build a REST API that's actually correct (not just running), understand databases, auth, and error handling. This is the path to **Senior Software Engineer**. Micro1 asks for backend, APIs, debugging, automated testing, and scalable services.

Recommended primary stack: **Python + FastAPI** (opens the road to AI APIs → LLM → RAG → Agents).

---

## 📚 Learn

### HTTP & REST
`HTTP methods` · `status codes` · `REST` · `CRUD` · `headers` · `idempotency` · `pagination`

### Auth & Security
`Authentication` · `JWT` · `OAuth basics` · `password hashing` · `CORS` · `rate limiting`

### Backend concepts
`Webhooks` · `Caching` · `Logging` · `Error handling` · `Background jobs` · `Environment variables`

### SQL & Database
`SELECT/JOIN` · `Transactions` · `Indexes` · `Migrations` · `N+1 problem` · `EXPLAIN ANALYZE`

### Free sources
- [Official FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) — primary source
- [FastAPI + SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [Roadmap.sh Backend](https://roadmap.sh/backend)
- [SQLBolt (interactive SQL)](https://sqlbolt.com/)
- [PostgreSQL Exercises](https://pgexercises.com/)
- [Official PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)

---

## 🧪 Exercise

Create the **`nael-api-lab`** repo — a REST API for one domain (e.g. todos, notes, or bookmarks):

- [ ] Full CRUD (GET/POST/PUT/PATCH/DELETE)
- [ ] Input validation with Pydantic
- [ ] JWT auth (register + login + protected route)
- [ ] Pagination + filtering + sorting
- [ ] Simple rate limiting
- [ ] Centralized error handling (custom exception handler)
- [ ] Structured logging
- [ ] A background job (e.g. send email / async processing)
- [ ] Tests: unit + integration (using TestClient)

---

## 🐛 Bug Hunt

Deliberately create classic backend bugs, then find & fix them:
- N+1 query (a loop querying the DB per item) → fix with eager loading.
- Endpoint without validation → weird input causes a 500.
- Race condition on a read-modify-write operation.

Write a regression test for each.

---

## 🤖 AI Challenge

Ask an AI to build 1 endpoint. Then inspect:
1. Is there input validation? SQL injection?
2. Are there tests?
3. Is error handling correct (right status codes)?
4. Is it efficient (number of queries)?

Fix it and write your evaluation in `evaluation/endpoint-review.md`.

---

## 📝 Evaluation

Take 2 versions of an endpoint implementation (yours vs the AI's). Compare with the rubric:

| Criterion | Weight |
|-----------|--------|
| Correctness | 40% |
| Edge cases | 20% |
| Security | 20% |
| Performance | 10% |
| Readability | 10% |

---

## 🏆 Final Task

`nael-api-lab` has:
- [ ] A complete API with auto-documentation (`/docs`)
- [ ] PostgreSQL (not SQLite) + migrations + indexes
- [ ] JWT auth + integration tests
- [ ] A README with architecture + how to run
- [ ] A green CI badge (continue in Level 3)

---

## ✅ Level 2 pass checklist

- [ ] Can explain the difference between 401 vs 403 vs 422 vs 500
- [ ] Understand why indexes matter and when to add one
- [ ] Can read `EXPLAIN ANALYZE`
- [ ] Can write integration tests for an API
- [ ] Understand the trade-off of JWT vs session
