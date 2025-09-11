"""
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:
- 1 <= s.length <= 5 * 10^4
- s contains printable ASCII characters.
- s does not contain any leading or trailing spaces.
- There is at least one word in s.
- All the words in s are separated by a single space.

Problem link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

from typing import List
import pytest


class Solution:
    def reverseWords(self, s: str) -> str:
        buffer = []

        wb, we = 0, 0
        while True:
            while we < len(s) and s[we] != " ":
                we += 1

            for i in range(we - 1, wb - 1, -1):
                buffer.append(s[i])

            if we < len(s):
                buffer.append(" ")

            wb = we + 1
            if wb >= len(s):
                break

            we = wb

        return "".join(buffer)

    def reverseWordsInOneLine(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    s = "Let's take LeetCode contest"
    expected = "s'teL ekat edoCteeL tsetnoc"
    assert sln.reverseWords(s) == expected


def test_example_2(sln):
    s = "God Ding"
    expected = "doG gniD"
    assert sln.reverseWords(s) == expected
