"""
LeetCode Problem 525: Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
"""


class Solution:
    def findMaxLength(self, nums):
        curr = ans = 0
        sums = {}
        for n in range(len(nums)):
            curr += 1 if nums[n] else -1
            if curr == 0:
                ans = max(ans, n + 1)
            elif curr in sums:
                ans = max(ans, n - sums[curr])
            else:
                sums[curr] = n
        return ans


import pytest


def test_example1():
    nums = [0, 1]
    expected = 2
    assert Solution().findMaxLength(nums) == expected


def test_example2():
    nums = [0, 1, 0]
    expected = 2
    assert Solution().findMaxLength(nums) == expected

def test_example3():
    nums = [0,1,1,1,1,1,0,0,0]
    expected = 6
    assert Solution().findMaxLength(nums) == expected
