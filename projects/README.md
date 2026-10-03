# Projects — Portfolio Konkret

Setiap level menghasilkan repo. Kumpulan ini jadi portfolio kamu saat apply Micro1.

| # | Repo | Level | Deskripsi | Status |
|---|------|-------|-----------|--------|
| 1 | `nael-algorithms` | 0–1 | DSA + Python, 25–40 soal, tiap soal ada test + analisis Big-O | `[ ]` |
| 2 | `nael-api-lab` | 2–3 | REST API FastAPI + PostgreSQL + JWT + Docker + CI/CD | `[ ]` |
| 3 | `agent-workflow-lab` | 4 | AI agent workflow + `AGENTS.md` + context engineering | `[ ]` |
| 4 | `ai-eval-kit` | 5–7 | AI coding evaluation toolkit (rubric, pairwise, hallucination) | `[ ]` |
| 5 | `coding-agent-eval` | 6 | Coding task + reference solution + deterministic verifier + harness | `[ ]` |
| 6 | `nael-go-api` | 8 | Go REST API + PostgreSQL + Docker + CI | `[ ]` |
| 7 | `nael-ai-lab` | 9 | RAG + agents + eval harness + observability + deploy | `[ ]` |
| 8 | `micro1-engineering-lab` | semua | Lab latihan gabungan (opsional, lihat bawah) | `[ ]` |

---

## Aturan tiap repo

Setiap repo portfolio **wajib** punya:

- [ ] README jelas: apa ini, kenapa dibuat, cara menjalankan, arsitektur.
- [ ] Test yang lewat.
- [ ] CI hijau (badge).
- [ ] Riwayat commit rapi (commit kecil, pesan jelas).
- [ ] Minimal 1 PR yang kamu review/merge sendiri.
- [ ] Tidak ada secret di kode.

---

## (Opsional) `micro1-engineering-lab`

Lab gabungan semua level dalam satu repo:

```
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

Tiap level berisi:

```
📚 Learn
🧪 Exercise
🐛 Bug
🤖 AI Challenge
📝 Evaluation
🏆 Final Task
```

Contoh alur challenge:

```
AI diberikan repository rusak.
AI harus: menemukan bug → membuat patch → menulis test
          → menjalankan test → memperbaiki
Kamu kemudian mengevaluasi AI-nya.
```

Itu melatih skill yang persis diminta beberapa listing Micro1.

---

## Checklist portfolio sebelum apply

- [ ] Semua repo punya README berkualitas
- [ ] Semua repo punya CI hijau
- [ ] Profil GitHub dirapikan (bio, pinned repos)
- [ ] Ada 1 PR open source merged (Level 7)
- [ ] Bisa menjelaskan tiap repo dalam 2 menit
