"""
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/

Two strings are considered close if you can attain one from the other using the following operations:

- Operation 1: Swap any two existing characters.
    - For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:
- 1 <= word1.length, word2.length <= 10^5
- word1 and word2 contain only lowercase English letters.
"""


from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Since we can't add or remove characters
        if len(word1) != len(word2):
            return False
        
        # Since we can't transform one character into non-existing character
        if set(word1) != set(word2):
            return False
        
        # Operation 1 allows us to freely sort strings, so we don't care about order of chars
        
        # Operation 2 allows us to swap frequencies
        # It means that we can't modify the frequency values, we can just rearrange them
        
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    word1 = "abc"
    word2 = "bca"
    assert solution.closeStrings(word1, word2) == True


def test_example_2(solution):
    word1 = "a"
    word2 = "aa"
    assert solution.closeStrings(word1, word2) == False


def test_example_3(solution):
    word1 = "cabbba"
    word2 = "abbccc"
    assert solution.closeStrings(word1, word2) == True
