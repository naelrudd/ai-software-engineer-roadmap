# Workshop 05 — Profile & optimize

> ⏱ ~90 min · 🎯 Measure first, then make it faster — and prove it.

Premature optimization wastes time. The rule: **measure, find the hotspot, fix it, measure again.**

---

## Part A — Timing

```python
import time


def timeit(fn, *args, repeat=5):
    best = float("inf")
    for _ in range(repeat):
        start = time.perf_counter()
        fn(*args)
        best = min(best, time.perf_counter() - start)
    return best
```

Use `perf_counter` (monotonic, high-resolution). Run multiple times and take the best to reduce noise.

For proper micro-benchmarks: `python -m timeit "code"`.

---

## Part B — Profiling

Find where time actually goes:

```bash
python -m cProfile -s cumtime exercises/two_sum/solution.py
```

Read the output: `tottime` (self time) and `cumtime` (including calls). The hotspot is usually obvious.

For line-level profiling: `pip install line_profiler` then `kernprof -l -v script.py`.

For memory: `pip install memory_profiler`.

---

## Part C — Guided optimization

Start from the brute-force two-sum:

```python
def two_sum_slow(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

1. **Measure** on `nums = list(range(5000))`, target beyond max (worst case).
2. **Profile** — you'll see the nested loop dominating.
3. **Hypothesize** — a hash map removes the inner loop.
4. **Implement** the O(n) version.
5. **Measure again** — record both numbers.

Write the before/after in a table:

| Version | Complexity | Time (n=5000) |
|---------|-----------|---------------|
| brute force | O(n²) | ? |
| hash map | O(n) | ? |

---

## Part D — Optimization rules

- Choose the right data structure first (biggest wins).
- Avoid work in loops (hoist invariants).
- Use comprehensions and builtins (`sum`, `any`, `max`) — they're C-speed.
- Cache repeated computation (`functools.lru_cache`).
- Don't micro-optimize what doesn't matter — profile first.

---

## Exercises

1. Benchmark brute-force vs hash-map two-sum; write the table.
2. Optimize `has_duplicates` from O(n²) to O(n); benchmark.
3. Use `cProfile` on a recursive Fibonacci and explain the output.
4. Add `@lru_cache` to a recursion; measure the speedup.
5. Take one of your earlier solutions and improve it; document the before/after.

---

## Deliverable

- [ ] `docs/optimization-log.md` with at least 2 before/after measurements
- [ ] Each optimization explained (what was slow, why the fix works)
- [ ] Tests still green after optimization
- [ ] Committed via PR

---

## Checklist

- [ ] Can time code with `perf_counter` / `timeit`
- [ ] Can read `cProfile` output
- [ ] Always measure before and after
- [ ] Know the common fast paths (builtins, comprehensions, caching)
- [ ] Wrote the optimization log
