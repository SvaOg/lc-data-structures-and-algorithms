# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python repository for LeetCode's Interview Crash Course - Data Structures and Algorithms. Each problem is a self-contained file with a docstring description, a `Solution` class, and pytest tests.

## Commands

```bash
# Run all tests
python -m pytest

# Run a single problem's tests
python -m pytest problems/trees_and_graphs/problem_721.py

# Run all tests in a category
python -m pytest problems/dynamic_programming/

# Run with verbose output
python -m pytest -v

# Format code
black .
```

Requires Python >= 3.12. The virtual environment is at `.venv/`.

## Architecture

Problems live in `problems/<topic>/` directories organized by algorithm category: arrays_and_strings, backtracking, binary_search, dynamic_programming, greedy, hasing, heaps, linked_lists, stacks_and_queues, trees_and_graphs.

Each `problem_NNN.py` file is self-contained: docstring with full problem description, `Solution` class, pytest fixture `sln`, and `test_001`/`test_002`/... functions.

### Shared Utilities

- `problems/trees_and_graphs/treenode.py` — `TreeNode` class with `create_from_list()` and `save_to_list()` class methods for binary tree serialization.
- `problems/linked_lists/linked_lists.py` — `ListNode` class with `build_linked_list()` and `linked_list_to_list()` helpers.

## Template Rules (from AGENTS.md)

When creating a new problem template:

- Filename: `problem_NNN.py` (no zero-padding)
- Header docstring: `[NUMBER]. [TITLE]`, full description, all examples, constraints, follow-ups
- Imports: only `from typing import List` and `import pytest`
- `class Solution` with correct method signature; body is `pass` (no implementation)
- `@pytest.fixture` named `sln` yielding `Solution()`
- One `test_NNN(sln)` per example, sequential naming, each with a short docstring
- No `if __name__ == "__main__"`, no parametrize, no implementation
- Canonical example: `problems/backtracking/problem_79.py`
- Place files where the user requests; ask for `problems/<topic>/` directory if unspecified

## Pytest Configuration

Tests are discovered from `problems/` directory. Files matching `problem_*.py` are collected as test modules. Strict markers and strict config are enforced.
