"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will
be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between
two words. The returned string should only have a single space separating the
words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single
space in the reversed string.

Constraints:
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve
it in-place with O(1) extra space?
"""

import pytest


class Solution:
    def reverseWords(self, s: str) -> str:
        buffer = []

        # Copy string to list, eliminating leading, trailing, and duplicated spaces
        for ch in s:
            if ch != " " or (buffer and buffer[-1] != " "):
                buffer.append(ch)

        if buffer[-1] == " ":
            buffer.pop()

        if not buffer:
            return ""

        # Reverse the whole string
        self._reverse(buffer, 0, len(buffer) - 1)

        # Reverse individual words back
        start = 0
        for end in range(len(buffer) + 1):
            if end == len(buffer) or buffer[end] == " ":
                self._reverse(buffer, start, end - 1)
                start = end + 1

        return "".join(buffer)

    def _reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test basic reversal of words."""
    assert sln.reverseWords("the sky is blue") == "blue is sky the"


def test_002(sln):
    """Test with leading and trailing spaces."""
    assert sln.reverseWords("  hello world  ") == "world hello"


def test_003(sln):
    """Test with multiple spaces between words."""
    assert sln.reverseWords("a good   example") == "example good a"
