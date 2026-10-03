# Level 1 — Git + Testing + Debugging

> 🎯 **Target:** bukan sekadar *"pernah pakai"*, tapi **bisa membuat test yang sengaja menangkap bug**. Beberapa role Micro1 eksplisit minta Git/GitHub workflow, PR, code review, branching, diff analysis, CI logs, dan automated testing.

---

## 📚 Learn

### Git
```
git clone      git branch     git checkout   git switch
git add        git commit     git diff       git log
git reset      git revert     git stash      git merge
git rebase     git cherry-pick
```

### GitHub
`Pull Request` · `Issues` · `Code Review` · `Actions` · `Releases` · `Tags`

### Testing
- **Python:** `pytest` · `fixtures` · `mock` · `unit test` · `integration test`
- **JS:** `Vitest` · `Jest`

### Debugging
`pdb` · breakpoint · watch variable · stack trace · binary search debugging · `git bisect`

### Sumber gratis
- [Pro Git Book (gratis)](https://git-scm.com/book/en/v2) — bab 1–3 wajib
- [Learn Git Branching (visual, interaktif)](https://learngitbranching.js.org/)
- [Oh Shit, Git!?!](https://ohshitgit.com/) — cara keluar dari masalah Git umum
- [GitHub Skills (kursus resmi interaktif)](https://github.com/skills)
- [GitHub Get Started](https://docs.github.com/en/get-started)
- [pytest docs](https://docs.pytest.org/en/stable/)
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pdb docs](https://docs.python.org/3/library/pdb.html)
- [Vitest Guide](https://vitest.dev/guide/)
- [Jest Getting Started](https://jestjs.io/docs/getting-started)

---

## 🧪 Exercise

### Git drills
Di repo `nael-algorithms`:
1. Buat branch `feat/array-two-sum`, commit, buka PR, review sendiri, merge.
2. Sengaja bikin konflik merge → selesaikan.
3. Latihan `rebase` branch di atas `main`, lalu `cherry-pick` satu commit.
4. Pakai `git bisect` untuk menemukan commit yang bikin test gagal.

### Testing drills
- Tulis test dengan `fixture` + `parametrize` + `mock`.
- Bikin 3 test yang **harus gagal** dulu (menangkap bug), baru perbaiki kodenya.
- Tulis 1 integration test yang memanggil API nyata (bukan mock).

---

## 🐛 Bug Hunt

Ambil kode orang (atau solusi AI), buat satu test yang membuktikan bug-nya, lalu:
```
1. git bisect untuk cari asal bug (kalau ada history)
2. tulis regression test
3. fix
4. pastikan semua test hijau
```

---

## 🤖 AI Challenge

Minta AI menulis kode **tanpa test**. Tugasmu:
1. Tulis test yang menguji edge case.
2. Temukan minimal 1 bug.
3. Tulis laporan: *"AI bilang X, padahal Y, karena Z."*

---

## 📝 Evaluation

Simulasi **code review**: ambil 1 PR AI-generated, review seperti senior engineer. Tulis komentar berisi: correctness, edge case, security, readability. Simpan di `reviews/pr-review-01.md`.

---

## 🏆 Final Task

- [ ] 1 PR nyata (branch → commit → PR → review → merge) terdokumentasi
- [ ] ≥ 20 test di `nael-algorithms`, termasuk fixtures & mock
- [ ] 3 regression test dari bug yang benar-benar ditemukan
- [ ] `reviews/` berisi minimal 1 code review tertulis

---

## ✅ Checklist lulus Level 1

- [ ] Bisa jelaskan `merge` vs `rebase` vs `cherry-pick` tanpa buka Google
- [ ] Nyaman pakai PR, review, dan branch workflow
- [ ] Bisa menulis test yang **gagal karena bug**, bukan cuma test yang lewat
- [ ] Bisa debugging pakai `pdb` / debugger, bukan `print()` doang
- [ ] Paham membaca CI logs
