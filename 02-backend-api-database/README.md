# Level 2 — Backend + API + Database

> 🎯 **Target:** bisa membangun REST API yang benar (bukan cuma jalan), paham database, auth, dan error handling. Ini jalan menuju **Senior Software Engineer**. Micro1 minta backend, API, debugging, automated testing, dan scalable services.

Stack utama yang disarankan: **Python + FastAPI** (membuka jalan ke AI APIs → LLM → RAG → Agents).

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

### Sumber gratis
- [FastAPI Tutorial resmi](https://fastapi.tiangolo.com/tutorial/) — sumber utama
- [FastAPI + SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [Roadmap.sh Backend](https://roadmap.sh/backend)
- [SQLBolt (SQL interaktif)](https://sqlbolt.com/)
- [PostgreSQL Exercises](https://pgexercises.com/)
- [PostgreSQL Tutorial resmi](https://www.postgresql.org/docs/current/tutorial.html)

---

## 🧪 Exercise

Bikin repo **`nael-api-lab`** — REST API untuk satu domain (mis. todo, notes, atau bookmarks):

- [ ] CRUD lengkap (GET/POST/PUT/PATCH/DELETE)
- [ ] Validasi input pakai Pydantic
- [ ] Auth JWT (register + login + protected route)
- [ ] Pagination + filtering + sorting
- [ ] Rate limiting sederhana
- [ ] Error handling terpusat (custom exception handler)
- [ ] Logging terstruktur
- [ ] Background job (mis. kirim email / proses async)
- [ ] Test: unit + integration (pakai TestClient)

---

## 🐛 Bug Hunt

Sengaja buat bug klasik backend, lalu temukan & perbaiki:
- N+1 query (loop yang query DB per item) → fix pakai eager loading.
- Endpoint tanpa validasi → input aneh bikin 500.
- Race condition pada operasi baca-ubah-tulis.

Tulis regression test untuk masing-masing.

---

## 🤖 AI Challenge

Minta AI membangun 1 endpoint. Lalu periksa:
1. Apakah ada validasi input? SQL injection?
2. Apakah ada test?
3. Apakah error handling benar (status code tepat)?
4. Apakah efisien (jumlah query)?

Perbaiki dan tulis evaluasinya di `evaluation/endpoint-review.md`.

---

## 📝 Evaluation

Ambil 2 versi implementasi endpoint (punyamu vs punya AI). Bandingkan dengan rubric:

| Kriteria | Bobot |
|----------|-------|
| Correctness | 40% |
| Edge cases | 20% |
| Security | 20% |
| Performance | 10% |
| Readability | 10% |

---

## 🏆 Final Task

`nael-api-lab` punya:
- [ ] API lengkap dengan dokumentasi otomatis (`/docs`)
- [ ] PostgreSQL (bukan SQLite) + migrasi + index
- [ ] Auth JWT + test integrasi
- [ ] README berisi arsitektur + cara menjalankan
- [ ] Badge CI hijau (lanjut ke Level 3)

---

## ✅ Checklist lulus Level 2

- [ ] Bisa jelaskan perbedaan 401 vs 403 vs 422 vs 500
- [ ] Paham kenapa index penting dan kapan bikin index
- [ ] Bisa membaca `EXPLAIN ANALYZE`
- [ ] Bisa menulis integration test untuk API
- [ ] Paham trade-off JWT vs session
