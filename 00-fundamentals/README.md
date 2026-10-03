# Level 0 — Programming Fundamentals

> 🎯 **Target:** you can look at someone else's code and say *"Okay, I understand what this program does"* — not just *"I could build it from scratch."* Micro1 work heavily involves review, debugging, code evaluation, and understanding unfamiliar codebases.

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

### Free sources
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [LearnPython.org (interactive)](https://www.learnpython.org/)
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [NeetCode Roadmap (structured DSA)](https://neetcode.io/roadmap)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [CP-Algorithms](https://cp-algorithms.com/)
- [Exercism Python Track](https://exercism.org/tracks/python)

### Tools
VS Code / Zed · Python · Node.js · Git · GitHub

---

## 🧪 Exercise

Create the **`nael-algorithms`** repo with this structure:

```
/arrays
/strings
/hashmaps
/trees
/graphs
/sorting
/searching
```

Each problem is one folder containing:

```
problem.md        # description + example input/output
solution.py       # your solution
test_solution.py  # pytest
README.md         # explanation + Big-O complexity
```

Target: **25–40 problems** spread across all folders.

---

## 🐛 Bug Hunt

Take a solution you wrote earlier and deliberately break an edge case (e.g. empty list, duplicates, negative integers). Write the test that catches the bug **before** fixing it. Document it in `README.md`.

---

## 🤖 AI Challenge

Ask an AI (OpenCode / [CC]) to solve 3 problems. Then:
1. Run the AI's solution.
2. Find at least 1 bug / missed edge case.
3. Write the test that proves it.
4. Fix it yourself — don't ask the AI to fix it.

---

## 📝 Evaluation

Create `evaluation/ai-solutions-review.md`: for each AI solution, score
`Correctness / Edge cases / Complexity / Readability` (0–5) + a short rationale.

---

## 🏆 Final Task

The `nael-algorithms` repo has:
- [ ] ≥ 25 problems, all with passing tests
- [ ] A per-problem README with Big-O analysis
- [ ] At least 3 tests that deliberately catch bugs
- [ ] A simple CI running pytest on every push (see Level 1/3)

---

## ✅ Level 0 pass checklist

- [ ] Python: typing, exceptions, async, generators used in real code
- [ ] TS/JS: understand Promise & closures, not memorized
- [ ] Can analyze the Big-O of your own solutions
- [ ] Can read someone's code and explain its flow
- [ ] `nael-algorithms` pushed to GitHub
