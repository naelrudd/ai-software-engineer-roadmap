# Level 8 — Go

> 🎯 **Target:** membuka pintu role **Software Engineer — Go/Python/TS $100–130/h**. Listing tersebut eksplisit menyebut **Go adalah primary language**, Python & TypeScript secondary.

---

## 📚 Learn

```
Go syntax      interfaces     structs        methods
error handling (idiomatik)    pointers
goroutines     channels       concurrency patterns
HTTP server    REST API       PostgreSQL     testing
Docker         GitHub Actions
```

### Peta belajar
```
Go syntax → interfaces → struct → goroutines → channels
   → HTTP server → REST API → PostgreSQL → testing → Docker
```

### Sumber gratis
- [A Tour of Go (interaktif, resmi)](https://go.dev/tour/)
- [Go by Example](https://gobyexample.com/)
- [Effective Go (resmi)](https://go.dev/doc/effective_go)
- [Learn Go with Tests (TDD)](https://quii.gitbook.io/learn-go-with-tests)
- [Roadmap.sh Go](https://roadmap.sh/golang)

---

## 🧪 Exercise

Bikin repo **`nael-go-api`** — REST API + PostgreSQL + Docker + GitHub Actions:

- [ ] HTTP server (stdlib atau chi/gin — pilih satu, pahami keduanya).
- [ ] CRUD endpoint + validasi input.
- [ ] Koneksi PostgreSQL (pakai `pgx` atau `database/sql`).
- [ ] Migrasi database.
- [ ] Auth middleware.
- [ ] Table-driven tests (idiomatik Go).
- [ ] Minimal 1 penggunaan goroutine + channel yang benar (mis. worker pool).
- [ ] Dockerfile multi-stage + docker compose.
- [ ] Workflow CI.

---

## 🐛 Bug Hunt

Bug klasik Go yang wajib kamu temukan & perbaiki:
- Race condition → deteksi pakai `go test -race`.
- Goroutine leak (channel tak ditutup / tanpa context).
- Loop variable capture (versi Go lama).
- Error diabaikan (`_ =` yang berbahaya).
- Nil pointer / slice aliasing.

Tulis regression test untuk masing-masing.

---

## 🤖 AI Challenge

Minta AI menulis kode Go konkuren. Periksa: ada race? ada goroutine leak? error handling benar? Pakai `go vet` + `-race`. Perbaiki + dokumentasikan.

---

## 📝 Evaluation

Bandingkan implementasi Go kamu vs AI di aspek: idiomatis, penanganan error, konkurensi aman, efisiensi. Simpan di `evaluation/go-review.md`.

---

## 🏆 Final Task

`nael-go-api` punya:
- [ ] REST API + PostgreSQL + migrasi
- [ ] Table-driven tests lulus, termasuk `-race`
- [ ] Dockerfile multi-stage + compose
- [ ] CI hijau
- [ ] README + benchmark sederhana

---

## ✅ Checklist lulus Level 8

- [ ] Paham goroutine vs thread dan kapan pakai channel vs mutex
- [ ] Bisa menulis test table-driven
- [ ] Paham error handling idiomatik Go (bukan try/catch)
- [ ] Bisa mendeteksi race condition
- [ ] Paham interface Go (implicit) dan kapan memakainya
