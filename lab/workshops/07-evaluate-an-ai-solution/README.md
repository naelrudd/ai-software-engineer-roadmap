# Workshop 07 — Evaluate an AI solution

> ⏱ ~90 min · 🎯 Find the bug an AI hid in code that "looks right".

This is the core skill for AI evaluation roles: judging AI output rigorously, not trusting it because it's fluent.

---

## Part A — The method

Given AI code, do this **every time**:

1. **Read for intent** — what does it claim to do?
2. **Read for correctness** — does the logic match the intent?
3. **Enumerate edge cases** — empty, single, duplicates, negatives, huge input.
4. **Run it** — on examples and edge cases.
5. **Write tests** — including the ones that fail.
6. **Score it** — with a rubric.
7. **Write a rationale** — specific, evidence-based.

---

## Part B — Guided hunt (3 AI solutions)

### Case 1 — Binary search

```python
def binary_search(a, target):
    lo, hi = 0, len(a)
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

Find the bug: mixed `[lo, hi)` range with `<=` and `hi = mid - 1` → can miss elements / go out of bounds. Write a failing test (e.g. search for the last element).

### Case 2 — Valid anagram

```python
def is_anagram(a, b):
    return sorted(a) == sorted(b)
```

Looks fine — but is it? Consider:
- Unicode normalization (`"é"` composed vs decomposed).
- Complexity O(n log n) vs O(n) with a count map.
- Case sensitivity (is that intended?).

Write the intended behavior and test it.

### Case 3 — Linked list reverse

```python
def reverse(head):
    prev = None
    while head:
        head.next = prev
        prev = head
        head = head.next
    return prev
```

Find the bug: `head.next` is overwritten before saving `head.next`, so traversal breaks (loses the rest of the list). Write a test that builds a 3-node list and catches it.

---

## Part C — The rubric

Score each AI solution:

| Criterion | Weight |
|-----------|--------|
| Correctness | 40% |
| Edge cases | 20% |
| Complexity | 15% |
| Readability | 15% |
| Tests present | 10% |

For each: score 0–5, multiply by weight, sum. Write a rationale with a **specific** error, not "it's wrong".

---

## Part D — Format

Create `evaluation/ai-review-01.md`:

```markdown
# AI solution review — binary search

## Claim
Returns the index of `target` or -1.

## Verdict
Incorrect. Fails for target at the last position.

## Failing test
<code>

## Root cause
Range invariant [lo, hi) mixed with `<=` and `hi = mid - 1`.

## Scores
- Correctness: 2/5 (40%) 
- Edge cases: 1/5 (20%)
- Complexity: 5/5 (15%)
- Readability: 4/5 (15%)
- Tests: 0/5 (10%)
Total: ...

## Correct version
<code>
```

---

## Exercises

1. Hunt all 3 cases above; write a review for each.
2. Ask an AI for a solution to any module exercise; review it.
3. Find one case where the AI is **correct** but you initially thought it was wrong — document it.
4. Write a reusable rubric in `evaluation/rubric.md`.

---

## Deliverable

- [ ] `evaluation/rubric.md`
- [ ] ≥ 3 written reviews in `evaluation/`
- [ ] A failing test for each bug found
- [ ] Committed via PR

---

## Checklist

- [ ] Never trust AI code without a test
- [ ] Can find subtle bugs (off-by-one, aliasing, mutation order)
- [ ] Write specific, evidence-based rationales
- [ ] Use a consistent rubric
- [ ] Documented at least 3 evaluations
