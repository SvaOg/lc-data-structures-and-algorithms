"""
2000. Reverse Prefix of Word

Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

- For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.

Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 2.
Reverse the part of word from 0 to 2 (inclusive), the resulting string is "zxyxxe".

Example 3:
Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

Constraints:
- 1 <= word.length <= 250
- word consists of lowercase English letters.
- ch is a lowercase English letter.

Problem link: https://leetcode.com/problems/reverse-prefix-of-word/
"""

import pytest


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        buffer = list(word)

        for pos in range(len(buffer)):
            if buffer[pos] == ch:
                break
        else:
            return word

        p1, p2 = 0, pos
        while p1 < p2:
            buffer[p1], buffer[p2] = buffer[p2], buffer[p1]
            p1 += 1
            p2 -= 1

        return "".join(buffer)

    def reversePrefix2(self, word: str, ch: str) -> str:
        """
        Happend to be slow
        """
        try:
            pos = word.index(ch)
            prefix = word[0 : pos + 1]
            suffix = word[pos + 1 :]
            return "".join(prefix[::-1] + suffix)
        except ValueError:
            return word


@pytest.fixture
def sln():
    return Solution()


def test_001():
    assert "abc".index("a") == 0
    with pytest.raises(ValueError):
        "abc".index("1")


def test_example_1(sln):
    word = "abcdefd"
    ch = "d"
    expected = "dcbaefd"
    assert sln.reversePrefix(word, ch) == expected


def test_example_2(sln):
    word = "xyxzxe"
    ch = "z"
    expected = "zxyxxe"
    assert sln.reversePrefix(word, ch) == expected


def test_example_3(sln):
    word = "abcd"
    ch = "z"
    expected = "abcd"
    assert sln.reversePrefix(word, ch) == expected
