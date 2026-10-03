# Level 5 — AI Evaluation

> 🎯 **Target:** evaluate AI output — compare answers, assign scores, write rationales, and find factual/technical errors. Not "how to use ChatGPT". AI evaluation roles ask for AI Agents, Rubric-Based Evaluation, Quality Assurance, and Process Improvement.

---

## 📚 Learn

### 1. Rubrics
Example weights:
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
AI says: *"React automatically caches this API request."*
You must be able to say: *"Incorrect. Here's why..."* — with evidence from docs/source.

### 4. Code evaluation
Check: `correct? · edge cases? · security? · performance? · maintainability? · tests?`

### Free sources
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) — many free eval courses
- [[OI] Evals (framework)](https://github.com/openai/evals)
- [promptfoo (LLM eval)](https://github.com/promptfoo/promptfoo)
- [HELM (Stanford, LLM eval)](https://crfm.stanford.edu/helm/)

---

## 🧪 Exercise

Create the **`ai-eval-kit`** repo:

- [ ] Write 3 different rubrics (coding task, technical Q&A, refactoring).
- [ ] Collect 20 pairs of AI output → score pairwise + write rationales.
- [ ] Find ≥ 5 technical hallucinations → document the correction + source.
- [ ] Evaluate 10 pieces of AI code: correctness, edge cases, security, performance.
- [ ] Build a reusable evaluation template (`templates/`).

---

## 🐛 Bug Hunt

Find AI output that **looks right but is wrong** (subtle bugs: off-by-one, wrong async, wrong lifetime, race condition). Write why it's wrong + a test/repro that proves it.

---

## 🤖 AI Challenge

Ask an AI to answer 5 technical questions (e.g. HTTP, Python async, SQL). Score its answers with your rubric. Focus: find errors that are **not** obvious.

---

## 📝 Evaluation

Create `scoring-sheet.md` containing:
- A definition of each criterion (so it's consistent across evaluators).
- Example scores of 0, 3, 5 for each criterion (anchors).
- Process: read → fact-check → score → rationale.

---

## 🏆 Final Task

`ai-eval-kit` has:
- [ ] ≥ 3 rubrics + evaluation templates
- [ ] ≥ 20 written evaluations with rationales
- [ ] ≥ 5 documented hallucinations + sourced corrections
- [ ] `scoring-sheet.md` with score anchors
- [ ] A README explaining the methodology

---

## ✅ Level 5 pass checklist

- [ ] Can write objective, specific evaluation rationales
- [ ] Can detect hallucinations and prove them
- [ ] Can judge AI code beyond "it runs/doesn't"
- [ ] Consistent when scoring (your scores match others')
- [ ] Understand evaluator bias (length bias, verbosity bias, sycophancy)
