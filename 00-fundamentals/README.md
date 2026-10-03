# Level 0 — Programming Fundamentals

> 🎯 **Target:** kamu bisa melihat kode orang lain dan berkata *"Oke, gue ngerti program ini melakukan apa"* — bukan cuma *"kalau bikin dari awal gue bisa"*. Pekerjaan Micro1 banyak minta review, debugging, code evaluation, dan memahami codebase asing.

---

## 📚 Learn

### Python
`functions` · `classes` · `exceptions` · `modules` · `typing` · `async/await` · `generators` · `file I/O` · `JSON` · `HTTP` · `logging`

### JavaScript / TypeScript
`async/await` · `Promise` · `closures` · `types` · `interfaces` · `generics` · `modules` · `error handling`

### Data Structures
`Array/List` · `HashMap/Dictionary` · `Stack` · `Queue` · `Set` · `Tree` · `Graph` · `Heap`

### Algorithms
`sorting` · `searching` · `recursion` · `BFS` · `DFS` · `two pointers` · `sliding window` · `binary search` · `basic DP` · `Big-O`

### Sumber gratis
- [Python Tutorial resmi](https://docs.python.org/3/tutorial/)
- [LearnPython.org (interaktif)](https://www.learnpython.org/)
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [NeetCode Roadmap (DSA terstruktur)](https://neetcode.io/roadmap)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [CP-Algorithms](https://cp-algorithms.com/)
- [Exercism Python Track](https://exercism.org/tracks/python)

### Tools
VS Code / Zed · Python · Node.js · Git · GitHub

---

## 🧪 Exercise

Bikin repo **`nael-algorithms`** dengan struktur:

```
/arrays
/strings
/hashmaps
/trees
/graphs
/sorting
/searching
```

Setiap problem satu folder berisi:

```
problem.md        # deskripsi + contoh input/output
solution.py       # solusi kamu
test_solution.py  # pytest
README.md         # penjelasan + kompleksitas Big-O
```

Target: **25–40 soal** tersebar di semua folder.

---

## 🐛 Bug Hunt

Ambil 1 solusi yang pernah kamu tulis, sengaja rusak edge case-nya (mis. list kosong, duplikat, integer negatif). Tulis test yang menangkap bug itu **sebelum** memperbaikinya. Dokumentasikan di `README.md`.

---

## 🤖 AI Challenge

Minta AI (OpenCode / [CC]) menulis solusi untuk 3 soal. Lalu:
1. Jalankan solusi AI.
2. Cari minimal 1 bug / edge case yang terlewat.
3. Tulis test yang membuktikannya.
4. Perbaiki sendiri — jangan minta AI memperbaiki.

---

## 📝 Evaluation

Bikin file `evaluation/ai-solutions-review.md`: untuk tiap solusi AI beri skor
`Correctness / Edge cases / Complexity / Readability` (0–5) + alasan singkat.

---

## 🏆 Final Task

Repo `nael-algorithms` punya:
- [ ] ≥ 25 soal, semua ada test dan lulus
- [ ] README per soal dengan analisis Big-O
- [ ] Minimal 3 test yang sengaja menangkap bug
- [ ] CI sederhana yang menjalankan pytest di setiap push (lihat Level 1/3)

---

## ✅ Checklist lulus Level 0

- [ ] Python: typing, exceptions, async, generator dipakai di kode nyata
- [ ] TS/JS: paham Promise & closure, bukan hafal
- [ ] Bisa analisis Big-O solusi sendiri
- [ ] Bisa baca kode orang dan menjelaskan alurnya
- [ ] `nael-algorithms` di-push ke GitHub
