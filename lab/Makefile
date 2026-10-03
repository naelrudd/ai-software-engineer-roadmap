.PHONY: help install test test-fast lint fmt cov clean new-problem

help:
	@echo "make install      - install dev dependencies"
	@echo "make test         - run the full test suite"
	@echo "make test-fast    - stop at first failure"
	@echo "make lint         - run ruff lint"
	@echo "make fmt          - auto-format with ruff"
	@echo "make cov          - run tests with coverage report"
	@echo "make new-problem  - scaffold a new exercise (PROBLEM=name)"
	@echo "make clean        - remove caches"

install:
	pip install -e ".[dev]"

test:
	pytest -q

test-fast:
	pytest -x -q

lint:
	ruff check .

fmt:
	ruff check --fix .
	ruff format .

cov:
	pytest --cov=. --cov-report=term-missing

new-problem:
	@test -n "$(PROBLEM)" || (echo "usage: make new-problem PROBLEM=two-sum" && exit 1)
	python scripts/new_problem.py "$(PROBLEM)"

clean:
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
