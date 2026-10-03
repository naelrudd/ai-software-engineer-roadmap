# Level 4 — AI-Assisted Software Engineering

> 🎯 **Target:** bukan *"AI bantu coding"*, tapi **mengontrol AI coding agent**. CV kamu sudah punya OpenCode / [CC] / Kiro — sekarang naik dari pemakai jadi operator. Micro1 eksplisit mencari orang yang terbiasa pakai AI assistants/agents dalam workflow developer.

---

## 📚 Learn

```
context engineering     prompt engineering      agent instructions
repository context      tool calling            MCP
subagents               verification            test-driven development
code review             diff review             plan mode
```

### Workflow ideal
```
AI Agent → Analyze repo → Plan → Implement → Run tests
   → Find failure → Fix → Run tests again → Review diff → Human approval
```

### Sumber gratis
- [Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [OpenCode Docs](https://opencode.ai/docs)
- [Prompt Engineering Overview (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

---

## 🧪 Exercise

Bikin repo **`agent-workflow-lab`**:

- [ ] Tulis `AGENTS.md` yang mengatur cara agent kerja di repo itu (konvensi, test command, larangan).
- [ ] Siapkan task nyata (mis. tambah fitur kecil), lalu jalankan agent end-to-end: plan → implement → test → fix.
- [ ] Dokumentasikan tiap langkah + di mana agent gagal dan kenapa.
- [ ] Bandingkan hasil dengan 2 pendekatan prompt berbeda (context sedikit vs lengkap).
- [ ] Buat 1 subagent / custom command (mis. `review-diff`, `write-tests`).

### Latihan context engineering
- Beri agent konteks **kurang** → amati halusinasi.
- Beri konteks **tepat** (file relevan + test) → amati akurasi.
- Tulis pelajaran di `docs/context-engineering.md`.

---

## 🐛 Bug Hunt

Minta agent memperbaiki bug. Sengaja jangan kasih test. Periksa:
- Apakah patch benar-benar menyelesaikan bug, atau cuma menutup gejala?
- Apakah ada regresi?
- Tulis test yang membuktikan patch benar/kurang.

---

## 🤖 AI Challenge

Desain "AI challenge" untuk dirimu sendiri: berikan repo rusak ke agent, minta ia memperbaiki, lalu **kamu nilai** hasilnya (correctness, ketepatan diff, kualitas test).

---

## 📝 Evaluation

Buat **rubric evaluasi diff AI**:

| Kriteria | Bobot |
|----------|-------|
| Apakah memperbaiki akar masalah | 35% |
| Tidak menimbulkan regresi | 25% |
| Kualitas test | 20% |
| Kejelasan diff | 10% |
| Efisiensi/kerapian | 10% |

Pakai untuk menilai 5 diff AI. Simpan di `evaluation/diff-scores.md`.

---

## 🏆 Final Task

- [ ] `agent-workflow-lab` dengan `AGENTS.md` + custom command/subagent
- [ ] `docs/context-engineering.md` berisi temuan nyata
- [ ] 5 diff AI dinilai dengan rubric
- [ ] Bisa menjelaskan kapan agent gagal dan cara memperbaiki konteksnya

---

## ✅ Checklist lulus Level 4

- [ ] Paham perbedaan prompt vs context engineering
- [ ] Bisa menulis `AGENTS.md` yang efektif
- [ ] Paham cara kerja tool calling & MCP
- [ ] Selalu verifikasi output agent dengan test, bukan percaya buta
- [ ] Bisa mengukur kualitas diff AI secara sistematis
