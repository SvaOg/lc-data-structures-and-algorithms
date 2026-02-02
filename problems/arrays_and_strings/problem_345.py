"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
"""

import pytest


class Solution:
    VOWELS = set(("a", "i", "e", "o", "u", "A", "I", "E", "O", "U"))

    def reverseVowels(self, s: str) -> str:
        n = len(s)
        result = list(s)
        left, right = 0, n - 1

        while left < right:
            while left < n and result[left] not in self.VOWELS:
                left += 1

            while right > 0 and result[right] not in self.VOWELS:
                right -= 1

            if left < right:
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1

        return "".join(result)


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    assert sln.reverseVowels("hello") == "holle"


def test_002(sln):
    """Test the second example from the problem description."""
    assert sln.reverseVowels("leetcode") == "leotcede"


def test_003(sln):
    """Test the second example from the problem description."""
    input = "Unglad, I tar a tidal gnu."
    expected = "unglad, i tar a tIdal gnU."
    assert sln.reverseVowels(input) == expected
