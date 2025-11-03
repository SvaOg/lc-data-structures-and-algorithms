# Agent Instructions

These instructions apply to the entire repository. Use them when generating or editing LeetCode problem templates.

## LeetCode Template Rules

- File naming: `problem_nnn.py` (no zero-padding, e.g., `problem_209.py` or `problem_1.py`).
- Location: create files where the user requests. If not specified, ask for the target directory (commonly under `problems/<topic>/`).
- Header: include full problem text from LeetCode training data:
  - First line: `[NUMBER]. [TITLE]`
  - Full description
  - All examples as shown (Input/Output)
  - Constraints
  - Follow-up (if present)
- Imports: `from typing import List` and `import pytest`.
- Solution class:
  - `class Solution:`
  - Exact method signature from the problem with proper type hints.
  - Method body must be `pass` (no implementation).
- Pytest fixture:
  - `@pytest.fixture`
  - `def sln():` that yields `Solution()`.
- Tests (one per example):
  - Named `test_example_1`, `test_example_2`, `test_example_3`, ...
  - Each takes `sln` and has a short docstring.
  - Use simple `assert` comparing the call to the example’s expected output.

## Do Not Include

- No `if __name__ == "__main__"` block.
- No algorithm implementation (keep method body as `pass`).
- No complex test logic.

## Conventions and Tips

- Extract the problem number from the filename or the user request; do not zero‑pad.
- Mirror the structure demonstrated by `problems/trees_and_graphs/problem_79.py`.
- When unsure about destination folder, ask the user to choose a category under `problems/`.

## Source of Truth

- Follow `leetcode_template_config.md` for exact structure and requirements.

