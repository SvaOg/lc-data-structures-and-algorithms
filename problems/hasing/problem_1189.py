"""
LeetCode Problem 1189: Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
- 1 <= text.length <= 10^4
- text consists of lower case English letters only.

"""

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        return min([counter[ch] for ch in "ban"] + [counter[ch] // 2 for ch in "lo"])


import pytest


@pytest.mark.parametrize(
    "text,expected",
    [
        ("nlaebolko", 1),
        ("loonbalxballpoon", 2),
        ("leetcode", 0),
    ],
)
def test_maxNumberOfBalloons(text, expected):
    assert Solution().maxNumberOfBalloons(text) == expected
