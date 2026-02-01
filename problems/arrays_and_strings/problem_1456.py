"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length

Problem link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""

from typing import List
import pytest


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        left = 0
        right = left + k - 1

        count = 0
        for ch in s[left : right + 1]:
            if ch in vowels:
                count += 1

        res = count

        while right < len(s) - 1:
            if s[left] in vowels:
                count -= 1

            left += 1
            right += 1

            if s[right] in vowels:
                count += 1

            res = max(res, count)

        return res


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    s = "abciiidef"
    k = 3
    expected = 3
    assert sln.maxVowels(s, k) == expected


def test_example_2(sln):
    s = "aeiou"
    k = 2
    expected = 2
    assert sln.maxVowels(s, k) == expected


def test_example_3(sln):
    s = "leetcode"
    k = 3
    expected = 2
    assert sln.maxVowels(s, k) == expected
