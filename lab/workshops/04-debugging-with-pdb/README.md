# Workshop 04 — Debugging with pdb

> ⏱ ~75 min · 🎯 Stop using `print()`. Debug like an engineer.

`pdb` is Python's built-in debugger. It lets you pause execution, inspect variables, step line by line, and change state — all without editing your code.

---

## Part A — The basics

### Start the debugger

```python
import pdb


def buggy(nums):
    total = 0
    for x in nums:
        pdb.set_trace()  # execution pauses here
        total += x
    return total
```

Or from the command line:

```bash
python -m pdb exercises/two_sum/solution.py
```

Or in pytest:

```bash
pytest --pdb                 # drop into pdb on failure
pytest --pdb -x              # stop at first failure
```

Or breakpoint() (Python 3.7+):

```python
breakpoint()  # same as pdb.set_trace()
```

---

## Part B — The commands that matter

| Command | Meaning |
|---------|---------|
| `n` | next line (step over) |
| `s` | step into function |
| `c` | continue until next breakpoint |
| `r` | run until current function returns |
| `l` | list source around current line |
| `p expr` | print an expression |
| `pp expr` | pretty-print |
| `w` | where am I? (stack trace) |
| `u` / `d` | move up/down the stack |
| `b file:line` | set a breakpoint |
| `b func` | break when `func` is called |
| `cl` | clear breakpoints |
| `q` | quit |

You only need `n`, `s`, `c`, `p`, `l`, `w` for 90% of debugging.

---

## Part C — Guided bug hunt

A deliberately broken function:

```python
def find_max(nums):
    best = 0
    for x in nums:
        if x > best:
            best = x
    return best
```

**Bug:** returns `0` for a list of all-negative numbers.

### Steps
1. Add `breakpoint()` before the loop.
2. `p nums`, then `n` a few times, `p best`.
3. Observe `best` never updates for negatives.
4. Fix: initialize `best = nums[0]` (and handle empty input).
5. Write a regression test: `assert find_max([-5, -2, -9]) == -2`.

This "init with 0" bug is extremely common. You just found it without `print()`.

---

## Part D — Debug a failing test

1. Write a test that fails unexpectedly.
2. Run `pytest --pdb -x`.
3. When it drops into pdb, use `w` to see the call stack, `p` to inspect locals.
4. Find the root cause, fix, re-run.

---

## Exercises

1. Fix `find_max` for negatives using `pdb`, not `print`.
2. Take a buggy linked-list `reverse` and find the pointer bug with `pdb`.
3. Use `pytest --pdb` on a test you wrote earlier that you can't explain.
4. Use a conditional breakpoint: `b solution.py:10, nums == []`.
5. Debug a function that mutates a shared default argument.

---

## Deliverable

- [ ] `docs/debugging-log.md` with 3 bugs you found, the pdb commands you used, and the root cause
- [ ] Regression test for each bug
- [ ] Committed via PR

---

## Checklist

- [ ] Comfortable with `n`, `s`, `c`, `p`, `l`, `w`
- [ ] Can use `breakpoint()` and `pytest --pdb`
- [ ] Can navigate the call stack with `u`/`d`
- [ ] Found at least one bug that `print()` would have missed
- [ ] Wrote the debugging log
