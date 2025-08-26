# LeetCode Problem Template Configuration

## Purpose
This file contains the exact instructions for generating LeetCode problem templates in this project. Copy this file to any new project to ensure consistent template generation.

## Template Structure Requirements

### 1. File Naming Convention
- Use format: `problem_0xxx.py` (e.g., `problem_0079.py`, `problem_0113.py`)
- Always use 4-digit zero-padded problem numbers

### 2. File Content Structure
Follow the exact pattern from `problem_0079.py`:

```python
"""
[PROBLEM_NUMBER]. [PROBLEM_TITLE]

[PROBLEM_DESCRIPTION]

Example 1:
[EXAMPLE_1_INPUT]
Output: [EXAMPLE_1_OUTPUT]

Example 2:
[EXAMPLE_2_INPUT]
Output: [EXAMPLE_2_OUTPUT]

Example 3:
[EXAMPLE_3_INPUT]
Output: [EXAMPLE_3_OUTPUT]

...

Constraints:
[CONSTRAINTS]

Follow up: [FOLLOW_UP_QUESTION]
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

def test_003(sln):
    """Test the third example from the problem description."""
    [TEST_3_CODE]
    assert sln.[METHOD_NAME]([PARAMETERS]) == [EXPECTED_RESULT]
```

### 3. Required Elements

#### Problem Header
- Complete problem description from LeetCode training data
- All examples with inputs and outputs
- All constraints
- Follow-up questions if present

#### Imports
- `from typing import List`
- `import pytest`

#### Solution Class
- Class named `Solution`
- Method signature exactly as specified in LeetCode problem
- Method body contains only `pass` statement
- Include proper type hints and return types

#### Pytest Fixture
- `@pytest.fixture` decorator
- Function named `sln`
- Yields `Solution()` instance

#### Test Functions
- Named `test_001`, `test_002`, `test_003`, etc.
- Each takes `sln` parameter
- Include docstring explaining what is being tested
- Use simple `assert` statements
- Test all examples from problem description
- Add edge case tests as appropriate

### 4. What NOT to Include
- No `if __name__ == "__main__"` block
- No implementation code (only `pass`)
- No complex test logic (keep tests simple)

## Usage Instructions

When asked to create a template for a specific LeetCode problem:

1. **Create the file** with correct naming convention
2. **Use LeetCode training data** for complete problem description
3. **Generate Solution class** with exact method signature from problem
4. **Create test cases** from all examples in problem description
5. **Follow this exact structure** for consistency

## Example Reference
See `tests/trees_and_graphs/problem_0079.py` for the complete working example of this template structure.
