"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""

from typing import List
import pytest


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s: List[str], opened, closed):
            if len(s) == 2 * n:
                result.append("".join(s))
                return

            if opened < n:
                backtrack(s + ["("], opened + 1, closed)

            if closed < opened:
                backtrack(s + [")"], opened, closed + 1)

        backtrack([], 0, 0)

        return result


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    n = 3
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    result = sln.generateParenthesis(n)
    # Sort both result and expected for comparison since order doesn't matter
    assert sorted(result) == sorted(expected)


def test_002(sln):
    """Test the second example from the problem description."""
    n = 1
    expected = ["()"]
    result = sln.generateParenthesis(n)
    assert result == expected


def test_003(sln):
    """Test edge case with n = 2."""
    n = 2
    expected = ["(())", "()()"]
    result = sln.generateParenthesis(n)
    assert sorted(result) == sorted(expected)


def test_004(sln):
    """Test edge case with n = 0."""
    n = 0
    expected = [""]
    result = sln.generateParenthesis(n)
    assert result == expected
