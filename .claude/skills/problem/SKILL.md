---
name: problem
description: Generate a LeetCode problem template file
argument-hint: <number> [topic-folder]
user-invocable: true
---

# Create template for LeetCode problem $ARGUMENTS[0]

## Instructions

1. **Determine the target folder.** If a second argument was provided (`$ARGUMENTS[1]`), use `problems/$ARGUMENTS[1]/`. Otherwise, ask the user which `problems/<topic>/` subdirectory to place the file in — list the existing subdirectories so they can pick one.

2. **Look up the problem.** Use your training data to find LeetCode problem number $ARGUMENTS[0]. You need: the title, full description text, all examples (Input/Output/Explanation), all constraints, and any follow-up questions.

3. **Create the file** at `problems/<topic>/problem_$ARGUMENTS[0].py` following the exact skeleton below. Do not zero-pad the number.

4. **After creating the file**, run `python -m pytest problems/<topic>/problem_$ARGUMENTS[0].py` to confirm the tests are collected (they will fail with `pass` bodies — that is expected).

## File skeleton

```python
"""
$NUMBER. $TITLE
https://leetcode.com/problems/$SLUG/

$FULL_DESCRIPTION

Example 1:
$EXAMPLE_1

...

Constraints:
$CONSTRAINTS
"""

from typing import List
import pytest


class Solution:
    def $METHOD_NAME(self, $PARAMETERS) -> $RETURN_TYPE:
        pass


@pytest.fixture
def sln():
    yield Solution()


@pytest.mark.xfail(reason="Not implemented", strict=True)
def test_001(sln):
    """Test the first example from the problem description."""
    assert sln.$METHOD_NAME($ARGS) == $EXPECTED


@pytest.mark.xfail(reason="Not implemented", strict=True)
def test_002(sln):
    """Test the second example from the problem description."""
    assert sln.$METHOD_NAME($ARGS) == $EXPECTED

# Add more test functions for remaining examples.
```

## Rules

- Import only `from typing import List` and `import pytest`. Add additional imports from `typing` only if the method signature requires them (e.g. `Optional`, `Dict`).
- If the problem uses trees, also import `from treenode import TreeNode` and use `TreeNode.create_from_list()` in tests.
- If the problem uses linked lists, also import `from linked_lists import ListNode, build_linked_list, linked_list_to_list` and use those helpers in tests.
- The `Solution` method body must be `pass` — never include an implementation.
- One `test_NNN(sln)` per example, named sequentially. Each test has a short docstring. Do not use `pytest.mark.parametrize`.
- Every test must be decorated with `@pytest.mark.xfail(reason="Not implemented", strict=True)`. Remove the decorator once the solution is implemented.
- No `if __name__ == "__main__"` block.
- Match the style of `problems/backtracking/problem_79.py`.
