"""
LeetCode Problem 643: Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Constraints:
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

Problem link: https://leetcode.com/problems/maximum-average-subarray-i/
"""

from typing import List
import pytest


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Args:
            nums (List[int]): The input array of integers.
            k (int): The length of the subarray.

        Returns:
            float: The maximum average value of a subarray of length k.
        """

        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for n in range(k, len(nums)):
            curr_sum += nums[n] - nums[n - k]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """
    Example 1: Basic test case from the problem description.
    """
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    assert abs(sln.findMaxAverage(nums, k) - 12.75) < 1e-5


def test_002(sln):
    """
    Edge case: All elements are the same.
    """
    nums = [5, 5, 5, 5, 5]
    k = 3
    assert abs(sln.findMaxAverage(nums, k) - 5.0) < 1e-5


def test_003(sln):
    """
    Edge case: Negative numbers.
    The maximum average subarray of length 2 is [-1, -12] = -6.5,
    [-12, -5] = -8.5, [-5, -6] = -5.5, [-6, -50] = -28.0, [-50, -3] = -26.5.
    The maximum is -5.5 from subarray [-5, -6].
    """
    nums = [-1, -12, -5, -6, -50, -3]
    k = 2
    assert abs(sln.findMaxAverage(nums, k) - (-5.5)) < 1e-5


def test_004(sln):
    """
    Edge case: k equals the length of the array.
    """
    nums = [1, 2, 3, 4, 5]
    k = 5
    assert abs(sln.findMaxAverage(nums, k) - 3.0) < 1e-5
