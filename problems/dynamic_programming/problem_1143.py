"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

from functools import cache
from typing import List
import pytest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = []
        for i in range(n + 1):
            dp.append([0] * (m + 1))

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]

    def longestCommonSubsequence_top_down(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return dp(i + 1, j + 1) + 1

            return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    text1 = "abcde"
    text2 = "ace"
    assert sln.longestCommonSubsequence(text1, text2) == 3


def test_002(sln):
    """Test the second example from the problem description."""
    text1 = "abc"
    text2 = "abc"
    assert sln.longestCommonSubsequence(text1, text2) == 3


def test_003(sln):
    """Test the third example from the problem description."""
    text1 = "abc"
    text2 = "def"
    assert sln.longestCommonSubsequence(text1, text2) == 0
