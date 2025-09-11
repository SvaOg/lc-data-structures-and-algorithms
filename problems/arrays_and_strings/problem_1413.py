"""
1413. Minimum Value to Get Positive Step by Step Sum

Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements from nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, the step by step sum would be:
    4 + (-3) = 1
    1 + 2 = 3
    3 + (-3) = 0  (less than 1, so not valid)
If you choose startValue = 5, the step by step sum would be:
    5 + (-3) = 2
    2 + 2 = 4
    4 + (-3) = 1
    1 + 4 = 5
    5 + 2 = 7
All step by step sums are greater than or equal to 1.
Hence, the minimum startValue is 5.

Example 2:
Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive. 

Example 3:
Input: nums = [1,-2,-3]
Output: 5

Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100

Problem link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
"""

from typing import List
import pytest


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        Given an array of integers nums, return the minimum positive value of startValue such that the step by step sum is never less than 1.

        :param nums: List[int] - The input array of integers.
        :return: int - The minimum positive start value.
        """
        curr_sum = nums[0]
        min_sum = curr_sum

        for n in range(1, len(nums)):
            curr_sum += nums[n]
            min_sum = min(min_sum, curr_sum)

        return max(1, 1 - min_sum)


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    nums = [-3, 2, -3, 4, 2]
    expected = 5
    assert sln.minStartValue(nums) == expected


def test_example_2(sln):
    nums = [1, 2]
    expected = 1
    assert sln.minStartValue(nums) == expected


def test_example_3(sln):
    nums = [1, -2, -3]
    expected = 5
    assert sln.minStartValue(nums) == expected
