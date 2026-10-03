# Level 6 — Coding-Agent Evaluation

> 🎯 **Target:** level paling cocok dengan arahmu. Micro1 punya role yang minta orang membuat coding tasks untuk AI, membuat reference solutions, debugging, serta membuat **deterministic verifiers**. Kamu tidak menulis kode — kamu menilai kode yang ditulis AI dan memverifikasinya.

---

## 📚 Learn

```
pytest              test fixtures       integration tests
mocking             property-based testing
regression tests    edge cases          deterministic verification
reference solution  patch review        scoring harness
```

### Format task
```
Task: "Fix authentication bug in this repository."
AI mengerjakan → kamu:
  1. Review patch
  2. Run tests
  3. Find hidden bug
  4. Create test
  5. Verify solution
```

### Sumber gratis
- [SWE-bench](https://www.swebench.com/) — benchmark coding agent
- [SWE-bench repo](https://github.com/princeton-nlp/SWE-bench)
- [HumanEval](https://github.com/openai/human-eval)
- [Hypothesis (property-based testing)](https://hypothesis.readthedocs.io/)
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

---

## 🧪 Exercise

Bikin repo **`coding-agent-eval`**:

- [ ] Siapkan 5 repo/task "rusak" (bug nyata, bukan mainan).
- [ ] Untuk tiap task: tulis reference solution sendiri.
- [ ] Tulis **deterministic verifier** (test yang hasilnya pasti, tidak flaky).
- [ ] Minta coding agent mengerjakan → jalankan verifier.
- [ ] Catat skor + alasan lulus/gagal.
- [ ] Bikin 3 property-based test pakai Hypothesis.

### Struktur tiap task
```
tasks/01-auth-bug/
├── README.md          # deskripsi task
├── reference.patch    # solusi referensi
├── verify/            # deterministic verifier
└── result.json        # hasil agent + skor
```

---

## 🐛 Bug Hunt

Ambil patch AI yang **lulus test kamu** tapi masih salah. Ini inti skill-nya:
- Verifier kamu terlalu lemah? Perkuat.
- Test lolos karena mock terlalu permisif? Perbaiki.
- Ada edge case yang belum diuji? Tambahkan.

---

## 🤖 AI Challenge

Minta agent membuat verifier untuk task yang kamu buat. Nilai verifier itu: apakah bisa membedakan solusi benar vs solusi "kelihatan benar"? Perbaiki versinya.

---

## 📝 Evaluation

Bikin `harness/` sederhana: jalankan semua task, kumpulkan skor agent, output tabel (lulus/gagal, alasan). Ini mini SWE-bench versi kamu.

---

## 🏆 Final Task

`coding-agent-eval` punya:
- [ ] 5 task + reference solution + verifier
- [ ] ≥ 3 property-based test
- [ ] Harness yang menghasilkan skor agregat
- [ ] Minimal 1 kasus di mana agent gagal dan kamu tahu kenapa
- [ ] README menjelaskan metodologi & batasan

---

## ✅ Checklist lulus Level 6

- [ ] Bisa menulis verifier yang deterministik (tidak flaky)
- [ ] Paham kenapa test bisa lolos padahal solusi salah
- [ ] Bisa membuat reference solution yang benar & minimal
- [ ] Bisa menilai kualitas patch di luar "test hijau"
- [ ] Paham dasar property-based testing
