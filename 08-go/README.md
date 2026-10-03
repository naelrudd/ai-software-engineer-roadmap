# Level 8 — Go

> 🎯 **Target:** open the door to **Go/Python/TS backend roles**. Some listings explicitly name **Go as the primary language**, with Python & TypeScript secondary. Go is also a common language in cloud, infra, and AI tooling.

> Not into Go? The same structure applies to deepening **TypeScript/Node** or learning **Rust** — pick one and go deep.

---

## 📚 Learn

```
Go syntax      interfaces     structs        methods
error handling (idiomatic)    pointers
goroutines     channels       concurrency patterns
HTTP server    REST API       PostgreSQL     testing
Docker         GitHub Actions
```

### Learning path
```
Go syntax → interfaces → struct → goroutines → channels
   → HTTP server → REST API → PostgreSQL → testing → Docker
```

### Free sources
- [A Tour of Go (interactive, official)](https://go.dev/tour/)
- [Go by Example](https://gobyexample.com/)
- [Effective Go (official)](https://go.dev/doc/effective_go)
- [Learn Go with Tests (TDD)](https://quii.gitbook.io/learn-go-with-tests)
- [Roadmap.sh Go](https://roadmap.sh/golang)

---

## 🧪 Exercise

Create the **`nael-go-api`** repo — REST API + PostgreSQL + Docker + GitHub Actions:

- [ ] HTTP server (stdlib or chi/gin — pick one, understand both).
- [ ] CRUD endpoints + input validation.
- [ ] PostgreSQL connection (`pgx` or `database/sql`).
- [ ] Database migrations.
- [ ] Auth middleware.
- [ ] Table-driven tests (idiomatic Go).
- [ ] At least 1 correct use of goroutine + channel (e.g. a worker pool).
- [ ] Multi-stage Dockerfile + docker compose.
- [ ] CI workflow.

---

## 🐛 Bug Hunt

Classic Go bugs you must find & fix:
- Race condition → detect with `go test -race`.
- Goroutine leak (channel not closed / missing context).
- Loop variable capture (older Go versions).
- Ignored errors (dangerous `_ =`).
- Nil pointer / slice aliasing.

Write a regression test for each.

---

## 🤖 AI Challenge

Ask an AI to write concurrent Go code. Check: any race? any goroutine leak? correct error handling? Use `go vet` + `-race`. Fix it + document.

---

## 📝 Evaluation

Compare your Go implementation vs the AI's on: idiomatic style, error handling, safe concurrency, efficiency. Save to `evaluation/go-review.md`.

---

## 🏆 Final Task

`nael-go-api` has:
- [ ] REST API + PostgreSQL + migrations
- [ ] Table-driven tests passing, including `-race`
- [ ] Multi-stage Dockerfile + compose
- [ ] Green CI
- [ ] README + a simple benchmark

---

## ✅ Level 8 pass checklist

- [ ] Understand goroutine vs thread and when to use channel vs mutex
- [ ] Can write table-driven tests
- [ ] Understand idiomatic Go error handling (not try/catch)
- [ ] Can detect race conditions
- [ ] Understand Go interfaces (implicit) and when to use them
