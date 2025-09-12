"""
1208. Get Equal Substrings Within Budget

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". The cost is 3, so the maximum length is 3.

Example 2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to t, so the maximum length is 1.

Example 3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.

Constraints:
- 1 <= s.length <= 10^5
- t.length == s.length
- 0 <= maxCost <= 10^6
- s and t only contain lower case English letters.

Problem link: https://leetcode.com/problems/get-equal-substrings-within-budget/
"""

import pytest


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0

        left, curr_cost = 0, 0

        costs = [0] * len(s)
        for right in range(len(s)):
            costs[right] = abs(ord(s[right]) - ord(t[right]))
            curr_cost += costs[right]
            while curr_cost > maxCost:
                curr_cost -= costs[left]
                left += 1
            res = max(res, right - left + 1)

        return res

    def equalSubstring2(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s, t)]

        res = 0

        left, curr_cost = 0, 0
        for right in range(len(costs)):
            curr_cost += costs[right]
            while curr_cost > maxCost:
                curr_cost -= costs[left]
                left += 1
            res = max(res, right - left + 1)

        return res


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    # "abc" -> "bcd", cost = 1+1+1=3
    expected = 3
    assert sln.equalSubstring(s, t, maxCost) == expected


def test_example_2(sln):
    s = "abcd"
    t = "cdef"
    maxCost = 3
    # Each char cost 2, so only 1 char can be changed
    expected = 1
    assert sln.equalSubstring(s, t, maxCost) == expected


def test_example_3(sln):
    s = "abcd"
    t = "acde"
    maxCost = 0
    # Only substrings with no cost, so max length is 1 (where s[i]==t[i])
    expected = 1
    assert sln.equalSubstring(s, t, maxCost) == expected
