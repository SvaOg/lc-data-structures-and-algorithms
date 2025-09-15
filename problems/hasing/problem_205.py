"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        match1, match2 = {}, {}
        for ch1, ch2 in zip(s, t):
            if match1.setdefault(ch1, ch2) != ch2 or match2.setdefault(ch2, ch1) != ch1:
                return False
        return True


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_001(solution):
    s = "badc"
    t = "baba"
    assert solution.isIsomorphic(s, t) == False


def test_example_1(solution):
    s = "egg"
    t = "add"
    assert solution.isIsomorphic(s, t) == True


def test_example_2(solution):
    s = "foo"
    t = "bar"
    assert solution.isIsomorphic(s, t) == False


def test_example_3(solution):
    s = "paper"
    t = "title"
    assert solution.isIsomorphic(s, t) == True
