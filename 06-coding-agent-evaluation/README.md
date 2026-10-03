# Level 6 — Coding-Agent Evaluation

> 🎯 **Target:** the level closest to the AI-evaluation frontier. Roles here ask you to create coding tasks for AI, write reference solutions, debug, and build **deterministic verifiers**. You don't write the code — you judge the code an AI wrote and verify it.

---

## 📚 Learn

```
pytest              test fixtures       integration tests
mocking             property-based testing
regression tests    edge cases          deterministic verification
reference solution  patch review        scoring harness
```

### Task format
```
Task: "Fix authentication bug in this repository."
AI does the work → you:
  1. Review the patch
  2. Run tests
  3. Find the hidden bug
  4. Create a test
  5. Verify the solution
```

### Free sources
- [SWE-bench](https://www.swebench.com/) — coding agent benchmark
- [SWE-bench repo](https://github.com/princeton-nlp/SWE-bench)
- [HumanEval](https://github.com/openai/human-eval)
- [Hypothesis (property-based testing)](https://hypothesis.readthedocs.io/)
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)

---

## 🧪 Exercise

Create the **`coding-agent-eval`** repo:

- [ ] Prepare 5 "broken" repos/tasks (real bugs, not toys).
- [ ] For each task: write the reference solution yourself.
- [ ] Write a **deterministic verifier** (a test with a certain, non-flaky result).
- [ ] Have a coding agent attempt it → run the verifier.
- [ ] Record the score + reason for pass/fail.
- [ ] Write 3 property-based tests with Hypothesis.

### Per-task structure
```
tasks/01-auth-bug/
├── README.md          # task description
├── reference.patch    # reference solution
├── verify/            # deterministic verifier
└── result.json        # agent result + score
```

---

## 🐛 Bug Hunt

Take an AI patch that **passes your test** but is still wrong. This is the core skill:
- Is your verifier too weak? Strengthen it.
- Does the test pass because the mock is too permissive? Fix it.
- Is there an untested edge case? Add it.

---

## 🤖 AI Challenge

Ask an agent to write a verifier for a task you created. Grade that verifier: can it tell a correct solution from a "looks correct" one? Improve it.

---

## 📝 Evaluation

Build a simple `harness/`: run all tasks, collect agent scores, output a table (pass/fail, reason). This is your mini SWE-bench.

---

## 🏆 Final Task

`coding-agent-eval` has:
- [ ] 5 tasks + reference solution + verifier
- [ ] ≥ 3 property-based tests
- [ ] A harness producing an aggregate score
- [ ] At least 1 case where the agent failed and you know why
- [ ] A README explaining methodology & limitations

---

## ✅ Level 6 pass checklist

- [ ] Can write a deterministic verifier (not flaky)
- [ ] Understand why a test can pass while the solution is wrong
- [ ] Can produce a correct & minimal reference solution
- [ ] Can judge patch quality beyond "tests are green"
- [ ] Understand the basics of property-based testing
