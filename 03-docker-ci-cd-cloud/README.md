# Level 3 — Docker + CI/CD + Cloud

> 🎯 **Target:** be able to say concretely *"I built and maintained CI/CD workflows"* — not just list GitHub Actions as a skill. Many engineering roles explicitly ask for CI/CD + Python/Bash + REST API + OAuth + webhooks + GitHub workflows.

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

### Free sources
- [Docker Get Started](https://docs.docker.com/get-started/)
- [Docker Curriculum](https://docker-curriculum.com/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [GitHub Skill: Hello GitHub Actions](https://github.com/skills/hello-github-actions)
- [The Twelve-Factor App](https://12factor.net/)

---

## 🧪 Exercise

Take one of your projects (e.g. `nael-api-lab`) and make it:

```
PR → GitHub Actions → pytest / Vitest → build → deployment
```

Tasks:
- [ ] Write a `Dockerfile` (multi-stage) for the API.
- [ ] Write a `docker-compose.yml` (API + PostgreSQL).
- [ ] CI workflow: install → lint → test → build.
- [ ] CD workflow: deploy to Railway/Render/Vercel.
- [ ] Store secrets in GitHub Secrets, **never** in code.
- [ ] Add a CI status badge to the README.

---

## 🐛 Bug Hunt

- Docker image too big (e.g. 1GB+) → fix with multi-stage + `.dockerignore`.
- Container works locally but fails in CI → find the cause (version, env, path, permissions).
- Flaky test in CI (sometimes passes, sometimes fails) → find the source of non-determinism.

---

## 🤖 AI Challenge

Ask an AI to generate a GitHub Actions workflow. Check:
1. Does it use pinned action versions (not `@master`)?
2. Does it cache dependencies?
3. Do secrets leak into logs?
4. Is the workflow safe for PRs from forks (permissions)?

Fix it + write notes in `evaluation/ci-review.md`.

---

## 📝 Evaluation

Build a CI/CD pipeline review checklist (security, speed, reliability). Save it to `docs/ci-checklist.md` — this is reusable for evaluation roles.

---

## 🏆 Final Task

- [ ] `docker compose up` works from scratch on a clean machine
- [ ] CI green on every PR + badge in README
- [ ] Automated deploy (staging/production)
- [ ] No secrets in the repo
- [ ] `docs/ci-checklist.md` complete

---

## ✅ Level 3 pass checklist

- [ ] Can write a Dockerfile without cheating
- [ ] Understand layer caching & why `COPY` order matters
- [ ] Can debug a failing CI pipeline
- [ ] Can deploy an API + database to a free cloud tier
- [ ] Understand 12-Factor principles (config via env)
