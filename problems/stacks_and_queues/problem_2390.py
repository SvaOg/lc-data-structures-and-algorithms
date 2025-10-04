"""
LeetCode Problem 2390: Removing Stars From a String

You are given a string s, which contains stars '*'.

In one operation, you can:

- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:

- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.

Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: 
- Remove the closest non-star character to the left of the first star, as well as the star itself, "leet**cod*e" becomes "lee*cod*e".
- Remove the closest non-star character to the left of the second star, as well as the star itself, "lee*cod*e" becomes "lecod*e".
- Remove the closest non-star character to the left of the third star, as well as the star itself, "lecod*e" becomes "lecoe".
There are no more stars, so we return "lecoe".

Example 2:
Input: s = "erase*****"
Output: ""
Explanation: 
- The entire string is removed, so we return an empty string.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters and stars '*'.
- The operation above can be performed on s.
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


import pytest

def test_example_1():
    """
    Example 1:
    Input: s = "leet**cod*e"
    Output: "lecoe"
    """
    sol = Solution()
    assert sol.removeStars("leet**cod*e") == "lecoe"

def test_example_2():
    """
    Example 2:
    Input: s = "erase*****"
    Output: ""
    """
    sol = Solution()
    assert sol.removeStars("erase*****") == ""
