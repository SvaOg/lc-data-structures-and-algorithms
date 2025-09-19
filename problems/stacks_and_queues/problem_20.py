"""
LeetCode Problem 20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "[": "]", "{": "}"}
        
        stack = []
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if pairs[prev] != ch:
                    return False

        return not stack

    def isValid1(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        
        stack = []
        for ch in s:
            match ch:
                case "(" | "[" | "{":
                    stack.append(ch)
                case _:
                    if not stack or stack.pop() != pairs[ch]:
                        return False

        return len(stack) == 0



import pytest


@pytest.mark.parametrize(
    "s,expected",
    [
        ("()", True),
    ],
)
def test_example_1(s, expected):
    assert Solution().isValid(s) == expected


@pytest.mark.parametrize(
    "s,expected",
    [
        ("()[]{}", True),
    ],
)
def test_example_2(s, expected):
    assert Solution().isValid(s) == expected


@pytest.mark.parametrize(
    "s,expected",
    [
        ("(]", False),
    ],
)
def test_example_3(s, expected):
    assert Solution().isValid(s) == expected


@pytest.mark.parametrize(
    "s,expected",
    [
        ("([)]", False),
    ],
)
def test_example_4(s, expected):
    assert Solution().isValid(s) == expected


@pytest.mark.parametrize(
    "s,expected",
    [
        ("{[]}", True),
    ],
)
def test_example_5(s, expected):
    assert Solution().isValid(s) == expected
