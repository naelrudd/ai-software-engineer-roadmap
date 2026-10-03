# Level 3 — Docker + CI/CD + Cloud

> 🎯 **Target:** bisa bilang secara konkret *"I built and maintained CI/CD workflows"* — bukan cuma menaruh GitHub Actions di daftar skill. Ada listing Micro1 yang eksplisit minta CI/CD + Python/Bash + REST API + OAuth + webhook + GitHub workflows.

---

## 📚 Learn

### Docker
```
Dockerfile      docker build    docker run      docker compose
volumes         networks        environment variables          healthcheck
multi-stage build               image size optimization
```

### GitHub Actions
```
push → workflow → install deps → run tests → lint → build → deploy
```

### Cloud / Deploy
`env vars & secrets` · `Vercel` · `Railway/Render` · `AWS basics (EC2, S3, RDS)` · `12-Factor App`

### Bash & scripting
`pipes` · `variables` · `loops` · `exit codes` · `set -euo pipefail`

### Sumber gratis
- [Docker Get Started](https://docs.docker.com/get-started/)
- [Docker Curriculum](https://docker-curriculum.com/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [GitHub Skill: Hello GitHub Actions](https://github.com/skills/hello-github-actions)
- [The Twelve-Factor App](https://12factor.net/)

---

## 🧪 Exercise

Ambil salah satu project (mis. `nael-api-lab` atau **KanvasHub**), jadikan:

```
PR → GitHub Actions → pytest / Vitest → build → deployment
```

Task:
- [ ] Tulis `Dockerfile` (multi-stage) untuk API.
- [ ] Tulis `docker-compose.yml` (API + PostgreSQL).
- [ ] Workflow CI: install → lint → test → build.
- [ ] Workflow CD: deploy ke Railway/Render/Vercel.
- [ ] Simpan secrets di GitHub Secrets, **jangan** di kode.
- [ ] Tambahkan badge status CI di README.

---

## 🐛 Bug Hunt

- Image Docker kegedean (mis. 1GB+) → perbaiki pakai multi-stage + `.dockerignore`.
- Container jalan lokal tapi gagal di CI → cari penyebab (versi, env, path, permission).
- Test flaky di CI (kadang lolos kadang gagal) → temukan sumber non-determinisme.

---

## 🤖 AI Challenge

Minta AI membuat workflow GitHub Actions. Periksa:
1. Apakah pakai versi action yang benar (bukan `@master`)?
2. Apakah caching dependency dipakai?
3. Apakah secrets bocor ke log?
4. Apakah workflow aman dari PR dari fork (permission)?

Perbaiki + tulis catatan di `evaluation/ci-review.md`.

---

## 📝 Evaluation

Buat checklist review pipeline CI/CD (security, kecepatan, keandalan). Simpan di `docs/ci-checklist.md` — ini reusable untuk role evaluasi.

---

## 🏆 Final Task

- [ ] `docker compose up` jalan dari nol di mesin bersih
- [ ] CI hijau di setiap PR + badge di README
- [ ] Ada deploy otomatis (staging/production)
- [ ] Secrets tidak ada di repo
- [ ] `docs/ci-checklist.md` selesai

---

## ✅ Checklist lulus Level 3

- [ ] Bisa menulis Dockerfile tanpa contekan
- [ ] Paham layer caching & kenapa urutan `COPY` penting
- [ ] Bisa debug pipeline CI yang gagal
- [ ] Bisa deploy API + database ke cloud gratis
- [ ] Paham prinsip 12-Factor (config via env)
