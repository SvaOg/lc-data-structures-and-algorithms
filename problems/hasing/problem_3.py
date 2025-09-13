"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans = 0

        left = 0
        chars = {}
        for right, ch in enumerate(s):
            pos = chars.get(ch, -1)
            if pos >= left:
                left = pos + 1
            ans = max(ans, right - left + 1)
            chars[ch] = right

        return ans

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not s:
            return 0

        ans = 0

        left = 0
        curr = set()
        for right, ch in enumerate(s):
            while ch in curr:
                curr.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)
            curr.add(ch)

        return ans


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3


def test_example_2(solution):
    assert solution.lengthOfLongestSubstring("bbbbb") == 1


def test_example_3(solution):
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
