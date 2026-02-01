"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.
"""

from collections import defaultdict
from typing import List
import pytest


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq1 = defaultdict(int)
        for ch in s1:
            freq1[ch] += 1

        freq2 = defaultdict(int)
        for ch in s2[: len(s1)]:
            freq2[ch] += 1

        if freq1 == freq2:
            return True

        start = 1
        end = start + len(s1) - 1
        while end < len(s2):
            ch = s2[start - 1]
            freq2[ch] -= 1
            if not freq2[ch]:
                del freq2[ch]

            freq2[s2[end]] += 1

            if freq1 == freq2:
                return True

            start += 1
            end += 1

        return False


@pytest.fixture
def solution():
    return Solution()


def test_001(solution):
    s1 = "abc"
    s2 = "cbad"
    expected = True
    assert solution.checkInclusion(s1, s2) == expected


def test_example_1(solution):
    s1 = "ab"
    s2 = "eidbaooo"
    assert solution.checkInclusion(s1, s2) == True


def test_example_2(solution):
    s1 = "ab"
    s2 = "eidboaoo"
    assert solution.checkInclusion(s1, s2) == False
