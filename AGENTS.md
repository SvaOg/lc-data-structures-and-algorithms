# Agent Instructions

These guidelines apply to every LeetCode problem template in this repository.

## Template Workflow
1. Create the file using the `problem_nnn.py` naming (no zero padding).
2. Work from the official LeetCode training data for the full description.
3. Copy the exact method signature into `class Solution`; leave the body as `pass`.
4. Add one pytest test per example from the description.
5. Match the structure demonstrated in `problems/trees_and_graphs/problem_79.py`.

## Template Rules
- Place the file where the user requests; if unspecified, ask them to choose a `problems/<topic>/` directory.
- The header must include `[NUMBER]. [TITLE]`, the complete description, every example (Input/Output), all constraints, and any follow-up text.
- Use only these imports: `from typing import List` and `import pytest`.
- Fixture: decorate `sln` with `@pytest.fixture` and yield `Solution()`.
- Tests: name them sequentially `test_001`, `test_002`, …; each takes `sln`, includes a short docstring, and asserts the method call equals the example’s expected output; do not parameterize.

## File Skeleton
Follow the exact layout below, adapting problem-specific details only:

```python
"""
[PROBLEM_NUMBER]. [PROBLEM_TITLE]

[PROBLEM_DESCRIPTION]

Example 1:
[EXAMPLE_1_INPUT]
Output: [EXAMPLE_1_OUTPUT]

...

Example N:
[EXAMPLE_N_INPUT]
Output: [EXAMPLE_N_OUTPUT]

...

Constraints:
[CONSTRAINTS]
"""

from typing import List
import pytest


class Solution:
    def [METHOD_NAME](self, [PARAMETERS]) -> [RETURN_TYPE]:
        pass


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    [TEST_1_CODE]
    assert sln.[METHOD_NAME]([PARAMETERS]) == [EXPECTED_RESULT]


def test_002(sln):
    """Test the second example from the problem description."""
    [TEST_2_CODE]
    assert sln.[METHOD_NAME]([PARAMETERS]) == [EXPECTED_RESULT]

# Add more tests for remaining examples.
```

## Prohibited Items
- No `if __name__ == "__main__"` block.
- No algorithm implementation—leave the solution method as `pass`.
- No complex or parameterized pytest logic.

## Additional Tips
- Always mirror the formatting of `problem_79.py`.
- Derive the problem number from the filename or request without zero padding.
- Confirm the destination directory with the user when unclear.
