"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you
want to check one by one to see if t has its subsequence. In this scenario, how would you
change your code?
"""

import pytest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        m, n = len(s), len(t)
        pos1, pos2 = 0, 0

        while pos1 < m and pos2 < n:
            if s[pos1] == t[pos2]:
                if pos1 == m - 1 and pos2 < n:
                    return True
                else:
                    pos1 += 1
                    pos2 += 1
            else:
                pos2 += 1

        return False


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    assert sln.isSubsequence("abc", "ahbgdc") is True


def test_002(sln):
    """Test the second example from the problem description."""
    assert sln.isSubsequence("axc", "ahbgdc") is False


def test_003(sln):
    assert sln.isSubsequence("abc", "tttabct") is True
