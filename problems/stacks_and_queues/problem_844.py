"""
LeetCode Problem 844: Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_backspaces(s):
            stack = []
            for ch in s:
                if ch == "#" and stack:
                    stack.pop()
                else:
                    stack.append(ch)
            return "".join(stack)

        return process_backspaces(s) == process_backspaces(t)


import pytest


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ab#c", "ad#c", True),
    ],
)
def test_example_1(s, t, expected):
    assert Solution().backspaceCompare(s, t) == expected


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ab##", "c#d#", True),
    ],
)
def test_example_2(s, t, expected):
    assert Solution().backspaceCompare(s, t) == expected


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("a#c", "b", False),
    ],
)
def test_example_3(s, t, expected):
    assert Solution().backspaceCompare(s, t) == expected
