"""
917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:

- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
- 1 <= s.length <= 100
- s consists of characters with ASCII values in the range [33, 122].
- s does not contain '\"' or '\\'.

Problem link: https://leetcode.com/problems/reverse-only-letters/
"""

import pytest


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        buffer = list(s)

        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            if not buffer[p1].isalpha():
                p1 += 1
            elif not buffer[p2].isalpha():
                p2 -= 1
            else:
                buffer[p1], buffer[p2] = buffer[p2], buffer[p1]
                p1 += 1
                p2 -= 1

        return "".join(buffer)

    def reverseOnlyLetters2(self, s: str) -> str:
        stack = [c for c in s if c.isalpha()]
        answer = [stack.pop() if ch.isalpha() else ch for ch in s]
        return "".join(answer)


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    s = "ab-cd"
    expected = "dc-ba"
    assert sln.reverseOnlyLetters(s) == expected


def test_example_2(sln):
    s = "a-bC-dEf-ghIj"
    expected = "j-Ih-gfE-dCba"
    assert sln.reverseOnlyLetters(s) == expected


def test_example_3(sln):
    s = "Test1ng-Leet=code-Q!"
    expected = "Qedo1ct-eeLg=ntse-T!"
    assert sln.reverseOnlyLetters(s) == expected
