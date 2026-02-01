"""
290. Word Pattern
https://leetcode.com/problems/word-pattern/

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", s = "dog dog dog dog"
Output: false

Constraints:
- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters.
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces.
- s does not contain leading or trailing spaces.
- All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        match1, match2 = {}, {}
        for ch, w in zip(pattern, words):
            if match1.setdefault(ch, w) != w or match2.setdefault(w, ch) != ch:
                return False

        return True


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_001(solution):
    pattern = "aaa"
    s = "aa aa aa aa"
    assert solution.wordPattern(pattern, s) == False


def test_example_1(solution):
    pattern = "abba"
    s = "dog cat cat dog"
    assert solution.wordPattern(pattern, s) == True


def test_example_2(solution):
    pattern = "abba"
    s = "dog cat cat fish"
    assert solution.wordPattern(pattern, s) == False


def test_example_3(solution):
    pattern = "aaaa"
    s = "dog cat cat dog"
    assert solution.wordPattern(pattern, s) == False


def test_example_4(solution):
    pattern = "abba"
    s = "dog dog dog dog"
    assert solution.wordPattern(pattern, s) == False
