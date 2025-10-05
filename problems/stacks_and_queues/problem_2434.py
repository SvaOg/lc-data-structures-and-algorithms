"""
LeetCode Problem 2434: Using a Robot to Print the Lexicographically Smallest String

You are given a string s and a robot that currently holds an empty string t. Apply the following operations until s and t are both empty:

- Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
- Remove the last character from the string t and append it to the answer string.

Return the lexicographically smallest string possible after applying the above operations.

Example 1:
Input: s = "zza"
Output: "azz"
Explanation:
Let p denote the position of the robot. Initially p = 0.
- Take the first character 'z' from s and append it to t: s = "za", t = "z"
- Take the first character 'z' from s and append it to t: s = "a", t = "zz"
- Take the first character 'a' from s and append it to t: s = "", t = "zza"
- Remove the last character from t and append it to answer: t = "zz", answer = "a"
- Remove the last character from t and append it to answer: t = "z", answer = "az"
- Remove the last character from t and append it to answer: t = "", answer = "azz"

Example 2:
Input: s = "bac"
Output: "abc"
Explanation:
- Take the first character 'b' from s and append it to t: s = "ac", t = "b"
- Since the first character of s ('a') is smaller than the last character of t ('b'), take 'a' from s and append it to t: s = "c", t = "ba"
- Remove the last character from t and append it to answer: t = "b", answer = "a"
- Since the first character of s ('c') is not smaller than the last character of t ('b'), remove the last character from t and append it to answer: t = "", answer = "ab"
- Take the first character 'c' from s and append it to t: s = "", t = "c"
- Remove the last character from t and append it to answer: t = "", answer = "abc"

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""

from collections import Counter

"""
ATTN: algorithm to find min_char left in the string
"""


class Solution:
    def robotWithString(self, s: str) -> str:
        res = []
        count = Counter(s)
        stack = []
        min_char = "a"
        for ch in s:
            stack.append(ch)
            count[ch] -= 1
            while min_char != "z" and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            while stack and stack[-1] <= min_char:
                res.append(stack.pop())
        return "".join(res)


import pytest


def test_example_1():
    """
    Example 1:
    Input: s = "zza"
    Output: "azz"
    """
    sol = Solution()
    assert sol.robotWithString("zza") == "azz"


def test_example_2():
    """
    Example 2:
    Input: s = "bac"
    Output: "abc"
    """
    sol = Solution()
    assert sol.robotWithString("bac") == "abc"


def test_3():
    input = "bydizfve"
    expected = "bdevfziy"
    assert expected == Solution().robotWithString(input)


def test_4():
    input = "vzhofnpo"
    expected = "fnohopzv"
    assert expected == Solution().robotWithString(input)
