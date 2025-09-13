"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters.
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        src = Counter(magazine)
        for ch, num in Counter(ransomNote).items():
            if not ch in src or src[ch] < num:
                return False
        return True


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.canConstruct("a", "b") == False


def test_example_2(solution):
    assert solution.canConstruct("aa", "ab") == False


def test_example_3(solution):
    assert solution.canConstruct("aa", "aab") == True
