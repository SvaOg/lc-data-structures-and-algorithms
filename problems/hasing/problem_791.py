"""
791. Custom Sort String
https://leetcode.com/problems/custom-sort-string/

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the returned string.

Return any permutation of s that satisfies this property.

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so they are sorted as "c", "b", "a". 
"d" does not appear in order, so it can be at any position in the returned string. 
"cbad", "bcad", "cbda", "bacd", "acbd", "abcd" are all valid outputs.

Example 2:
Input: order = "bcafg", s = "abcd"
Output: "bcad"
Explanation: 
"b", "c", "a" appear in order, so they are sorted as "b", "c", "a". 
"d" does not appear in order, so it can be at any position in the returned string.

Constraints:
- 1 <= order.length <= 26
- 1 <= s.length <= 200
- order and s consist of lowercase English letters.
- All the characters of order are unique.
"""

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = []
        for ch in order:
            if ch in freq:
                res.extend([ch] * freq[ch])
                del freq[ch]
        for ch, f in freq.items():
            res.extend([ch] * f)
        return "".join(res)


import pytest

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    order = "cba"
    s = "abcd"
    # Output can be any permutation that puts c, b, a in that order, d anywhere
    result = solution.customSortString(order, s)
    # Check that result is a permutation of s and c, b, a are in order
    assert sorted(result) == sorted(s)
    c_idx = result.find('c')
    b_idx = result.find('b')
    a_idx = result.find('a')
    assert c_idx < b_idx < a_idx

def test_example_2(solution):
    order = "bcafg"
    s = "abcd"
    result = solution.customSortString(order, s)
    assert sorted(result) == sorted(s)
    b_idx = result.find('b')
    c_idx = result.find('c')
    a_idx = result.find('a')
    assert b_idx < c_idx < a_idx
