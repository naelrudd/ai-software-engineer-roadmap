# Module 00 — Python refresh

> ⏱ ~4h · 🎯 Write Python that a reviewer would call idiomatic.

## Why this matters

Everything later depends on this. The goal is not "I know Python" but "I write Python that is clear, typed, tested, and hard to break."

---

## Core concepts

### Type hints
```python
def add(a: int, b: int) -> int:
    return a + b


def names(items: list[dict[str, str]]) -> set[str]:
    return {i["name"] for i in items}


# optional and unions (3.10+)
def find(x: int, data: list[int]) -> int | None: ...
```

Type hints are documentation the interpreter can check with tools (mypy/pyright). They make refactors safe.

### Exceptions
```python
try:
    value = int(raw)
except ValueError as e:
    raise ValueError(f"not an int: {raw!r}") from e
finally:
    cleanup()
```

Rules: raise specific exceptions, never bare `except:`, use `from e` to keep the cause.

### Comprehensions & generators
```python
squares = [x * x for x in range(10) if x % 2 == 0]
lookup = {x: x * x for x in range(5)}
evens = (x for x in range(10**9) if x % 2 == 0)  # lazy, constant memory
```

### Iterators & generators
```python
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip("\n")
```

`yield` gives you lazy sequences — the basis of streaming and pipelines.

### Dataclasses
```python
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    tags: list[str] = field(default_factory=list)
```

Less boilerplate than writing `__init__`/`__repr__` by hand.

### Context managers
```python
with open("f.txt") as f:  # always close, even on error
    data = f.read()
```

### `enumerate`, `zip`, `sorted(key=...)`
```python
for i, x in enumerate(items):
    ...

for name, score in zip(names, scores):
    ...

people.sort(key=lambda p: (-p.score, p.name))
```

### `collections`
```python
from collections import Counter, defaultdict, deque

Counter("aabbb")  # Counter({'b': 3, 'a': 2})
d = defaultdict(list)
d[k].append(v)
q = deque([1, 2, 3])
q.popleft()
```

### `__main__` guard
```python
def main() -> None: ...


if __name__ == "__main__":
    main()
```

---

## Common pitfalls

- Mutable default arguments: `def f(x, acc=[])` — shares the list across calls. Use `None` + create inside.
- `is` vs `==`: `is` is identity, `==` is value.
- Integer division `//` vs `/`.
- Modifying a list while iterating it.
- Shadowing builtins (`list`, `sum`, `id`, `type`).
- Late binding in closures/loops: capture loop vars via default arg or factory.
- Assuming dict/set order matters in old code (it's ordered since 3.7, but don't rely on it for logic).

---

## Exercises

1. Write `word_count(text) -> dict[str, int]` using `Counter`. Test with punctuation and case.
2. Write a generator `fib() -> Iterator[int]` that yields Fibonacci numbers lazily; take the first 10 with `itertools.islice`.
3. Write a `@dataclass` `Student` and sort a list by grade desc, then name asc.
4. Write `safe_divide(a, b)` that raises `ValueError` with a clear message on divide-by-zero.
5. Refactor a function with a mutable default arg bug; write a test that proves the bug existed.

---

## Paired workshop

[Workshop 01 — Git & repo setup](../../workshops/01-git-and-repo-setup/README.md)

## Checklist

- [ ] Can write typed functions and dataclasses without looking up syntax
- [ ] Understand generators vs lists (and when memory matters)
- [ ] Never use mutable default arguments
- [ ] Reach for `collections` before hand-rolling
- [ ] Wrote 3 lines in `NOTES.md` explaining the key ideas
