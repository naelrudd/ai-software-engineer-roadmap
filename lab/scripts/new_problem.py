"""Scaffold a new exercise from templates/problem.

Each exercise is a Python package (it gets an ``__init__.py``) so its
``solution.py`` never collides with another exercise's ``solution.py``.

Usage:
    python scripts/new_problem.py two_sum
    python scripts/new_problem.py two-sum       # hyphen is converted to _
    make new-problem PROBLEM=two_sum
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "problem"
EXERCISES = ROOT / "exercises"


def slugify(name: str) -> str:
    """Make a valid Python package name from a problem name."""
    cleaned = name.strip().strip("/").replace("-", "_").replace(" ", "_")
    if not cleaned.isidentifier():
        raise ValueError(f"'{name}' cannot be turned into a valid package name")
    return cleaned


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python scripts/new_problem.py <problem-name>")
        return 1

    try:
        slug = slugify(sys.argv[1])
    except ValueError as e:
        print(f"error: {e}")
        return 1

    dest = EXERCISES / slug
    if dest.exists():
        print(f"error: {dest} already exists")
        return 1

    shutil.copytree(TEMPLATE, dest)
    (dest / "__init__.py").touch()  # make it a package

    # Replace the placeholder problem name in the scaffolded files.
    for path in dest.iterdir():
        if path.is_file():
            text = path.read_text()
            path.write_text(text.replace("<Problem name>", slug))

    print(f"created {dest.relative_to(ROOT)}/")
    print("next:")
    print(f"  1. edit {dest.relative_to(ROOT)}/problem.md")
    print(f"  2. write tests first in {dest.relative_to(ROOT)}/test_solution.py")
    print("  3. implement solution.py")
    print("  4. run: make test")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
