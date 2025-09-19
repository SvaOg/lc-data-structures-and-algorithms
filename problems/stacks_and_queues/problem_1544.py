"""
LeetCode Problem 1544: Make The String Great

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

    0 <= i <= s.length - 2
    s[i] and s[i + 1] are the same letter, but in different cases.

To make the string great, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"

Constraints:
- 1 <= s.length <= 100
- s contains only lower and upper case English letters.
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack:
                prev = stack[-1]
                if ch.lower() == prev.lower() and ch != prev:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        return "".join(stack)


import pytest


@pytest.mark.parametrize(
    "s, expected",
    [
        ("leEeetcode", "leetcode"),
    ],
)
def test_example_1(s, expected):
    assert Solution().makeGood(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abBAcC", ""),
    ],
)
def test_example_2(s, expected):
    assert Solution().makeGood(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("s", "s"),
    ],
)
def test_example_3(s, expected):
    assert Solution().makeGood(s) == expected
