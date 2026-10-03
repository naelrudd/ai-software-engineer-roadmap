# Workshop 03 — Fixtures & parametrize

> ⏱ ~75 min · 🎯 Write tests that are expressive and don't repeat setup.

## Part A — `parametrize`

One test body, many cases. On failure, pytest tells you exactly which case.

```python
import pytest


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("", True),
        ("a", True),
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected
```

### Multiple parameters

```python
@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [10, 20])
def test_add(a, b):
    assert add(a, b) == a + b  # 3 x 2 = 6 cases
```

### Mark expected failures

```python
@pytest.mark.parametrize(
    ("nums", "target"),
    [([], 5), ([1], 1)],
)
def test_raises_on_bad_input(nums, target):
    with pytest.raises(ValueError):
        two_sum(nums, target)
```

---

## Part B — Fixtures

Fixtures provide setup/teardown and are injected by name.

```python
import pytest


@pytest.fixture
def sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    return root


def test_depth(sample_tree):
    assert max_depth(sample_tree) == 2
```

### Scope

```python
@pytest.fixture(scope="module")  # built once per test file
def big_array():
    return list(range(100_000))
```

Scopes: `function` (default), `class`, `module`, `session`.

### Yield fixtures (teardown)

```python
@pytest.fixture
def temp_file(tmp_path):
    f = tmp_path / "data.txt"
    f.write_text("hello")
    yield f
    f.unlink()  # teardown
```

### `tmp_path`

A fresh temporary directory per test — never write test files into the repo.

---

## Part C — When NOT to use a fixture

If setup is one line and used once, just write it inline. Fixtures are for shared or complex setup.

---

## Exercises

1. Convert 3 existing tests to `parametrize`. Count how many lines you save.
2. Add a fixture that builds a small graph used by 4 tests.
3. Add a `tmp_path`-based test that reads/writes a file.
4. Add a `pytest.raises` test for invalid input.
5. Add a `@pytest.fixture(scope="module")` for a large shared input; verify it's built once (add a print in setup and run with `-s`).

---

## Deliverable

- [ ] At least 2 test files using `parametrize`
- [ ] At least 1 fixture (function scope) and 1 module-scope fixture
- [ ] At least 1 `tmp_path` test
- [ ] Committed via PR

---

## Checklist

- [ ] Can parametrize a test with a table of cases
- [ ] Understand fixture scopes
- [ ] Know `yield` fixtures for teardown
- [ ] Use `tmp_path` instead of writing into the repo
- [ ] `make test -q` runs everything cleanly
