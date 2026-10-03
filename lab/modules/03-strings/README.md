# Module 03 — Strings

> ⏱ ~3h · 🎯 Manipulate text without accidentally going O(n²).

## Why this matters

String problems are everywhere (parsing, validation, search) and hide performance traps. This module builds the reflexes.

---

## Core concepts

### Strings are immutable

```python
s = "abc"
s[0] = "z"  # TypeError
s = "z" + s[1:]  # creates a new string
```

Immutability means each concatenation copies. Building a string in a loop is O(n²).

```python
# bad
out = ""
for c in s:
    out += c.upper()  # O(n^2)

# good
out = "".join(c.upper() for c in s)  # O(n)
```

### Useful operations

```python
s.lower()
s.upper()
s.strip()
s.split(",")
",".join(parts)
s.startswith("x")
s.endswith("y")
s.find("x")
s.replace("a", "b")
s.isalpha()
s.isdigit()
```

### Character ↔ code point

```python
ord("a")  # 97
chr(97)  # "a"
```

Useful for frequency arrays of size 26 for lowercase letters.

### Frequency counting

```python
from collections import Counter

Counter("anagram")  # Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})
```

### Two pointers on strings

Palindromes, reversals, and comparisons often use `lo`/`hi`.

```python
def is_palindrome(s):
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True
```

### Sliding window preview

Substring problems (longest unique substring, anagrams in a string) use a window — full treatment in [Module 14](../14-sliding-window/README.md).

---

## Common pitfalls

- `+=` string concatenation in a loop → O(n²).
- Comparing `s.lower()` repeatedly instead of once.
- Forgetting Unicode: `len("👍")` may surprise you (it's 1 in Python 3, but grapheme clusters aren't).
- Assuming ASCII — decide your alphabet and document it.
- Off-by-one in substrings (`s[i:j]` excludes `j`).

---

## Exercises

1. **Valid anagram** — frequency map, O(n).
2. **Valid palindrome** — two pointers, ignore non-alphanumeric.
3. **Reverse words** — split, reverse, join; keep O(n).
4. **First non-repeating character** — one pass + count.
5. **Longest common prefix** — across a list of strings.
6. **Isomorphic strings** — two maps both directions.

---

## Paired workshop

[Workshop 03 — Fixtures & parametrize](../../workshops/03-fixtures-and-parametrize/README.md)

## Checklist

- [ ] Never concatenate strings in a loop
- [ ] Comfortable with `Counter` and `ord`/`chr`
- [ ] Can write a two-pointer string check
- [ ] Test Unicode / empty / single-char cases
- [ ] Wrote 3 lines in `NOTES.md`
