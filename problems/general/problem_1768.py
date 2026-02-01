"""
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/

You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. If a string is longer than the
other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

Constraints:
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.
"""

import pytest
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))


class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for char1, char2 in zip(word1, word2):
            result.append(char1)
            result.append(char2)

        n = len(result) // 2
        result.append(word1[n:])
        result.append(word2[n:])

        return "".join(result)


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test merging two strings of equal length."""
    assert sln.mergeAlternately("abc", "pqr") == "apbqcr"


def test_002(sln):
    """Test merging when word2 is longer."""
    assert sln.mergeAlternately("ab", "pqrs") == "apbqrs"


def test_003(sln):
    """Test merging when word1 is longer."""
    assert sln.mergeAlternately("abcd", "pq") == "apbqcd"
