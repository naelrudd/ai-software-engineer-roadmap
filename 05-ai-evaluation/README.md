# Level 5 — AI Evaluation

> 🎯 **Target:** ini **entry point** kamu. Bukan "cara pakai ChatGPT", tapi mengevaluasi output AI: membandingkan jawaban, memberi penilaian, menulis rationale, dan menemukan factual/technical errors. Role AI Evaluation Specialist minta AI Agents, Rubric-Based Evaluation, Quality Assurance, Process Improvement.

---

## 📚 Learn

### 1. Rubric
Contoh bobot:
```
Correctness       40%
Completeness      20%
Code quality      15%
Security          10%
Performance       10%
Communication      5%
```

### 2. Pairwise evaluation
```
Answer A vs Answer B → Which is better? Why? What specific error exists?
```

### 3. Hallucination detection
AI bilang: *"React automatically caches this API request."*
Kamu harus bisa bilang: *"Incorrect. Here's why..."* — dengan bukti dari docs/source.

### 4. Code evaluation
Cek: `correct? · edge cases? · security? · performance? · maintainability? · tests?`

### Sumber gratis
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) — banyak course eval gratis
- [[OI] Evals (framework)](https://github.com/openai/evals)
- [promptfoo (eval LLM)](https://github.com/promptfoo/promptfoo)
- [HELM (Stanford, eval LLM)](https://crfm.stanford.edu/helm/)

---

## 🧪 Exercise

Bikin repo **`ai-eval-kit`**:

- [ ] Tulis 3 rubric berbeda (coding task, Q&A teknis, refactoring).
- [ ] Kumpulkan 20 pasang output AI → nilai pairwise + tulis rationale.
- [ ] Temukan ≥ 5 hallucination teknis → dokumentasikan koreksi + sumber.
- [ ] Evaluasi 10 potong kode AI: correctness, edge case, security, performance.
- [ ] Bikin template evaluasi yang bisa dipakai berulang (`templates/`).

---

## 🐛 Bug Hunt

Cari output AI yang **kelihatan benar tapi salah** (subtle bug: off-by-one, salah async, salah lifetime, race condition). Tulis kenapa salah + test/repro yang membuktikan.

---

## 🤖 AI Challenge

Minta AI menjawab 5 pertanyaan teknis (mis. soal HTTP, Python async, SQL). Nilai jawabannya pakai rubric kamu. Fokus: temukan error yang **tidak** terlihat jelas.

---

## 📝 Evaluation

Bikin `scoring-sheet.md` berisi:
- Definisi tiap kriteria (biar konsisten antar-evaluator).
- Contoh skor 0, 3, 5 untuk tiap kriteria (anchor).
- Proses: baca → cek fakta → skor → rationale.

---

## 🏆 Final Task

`ai-eval-kit` punya:
- [ ] ≥ 3 rubric + template evaluasi
- [ ] ≥ 20 evaluasi tertulis dengan rationale
- [ ] ≥ 5 hallucination terdokumentasi + koreksi bersumber
- [ ] `scoring-sheet.md` dengan anchor skor
- [ ] README yang menjelaskan metodologi

---

## ✅ Checklist lulus Level 5

- [ ] Bisa menulis rationale evaluasi yang objektif & spesifik
- [ ] Bisa mendeteksi hallucination dan membuktikannya
- [ ] Bisa menilai kode AI di luar aspek "jalan/tidak"
- [ ] Konsisten saat menilai (skor orang lain mirip)
- [ ] Paham bias evaluator (length bias, verbosity bias, sycophancy)
