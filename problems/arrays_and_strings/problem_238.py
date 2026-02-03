"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
  integer.

Follow-up: Can you solve the problem in O(1) extra space complexity? (The
output array does not count as extra space for space complexity analysis.)
"""

import pytest
from typing import List
from itertools import accumulate
import operator


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        prefix = list(accumulate(nums, operator.mul))
        suffix = list(accumulate(nums[::-1], operator.mul))[::-1]

        result = []
        for i in range(n):
            n1 = 1 if i == 0 else prefix[i - 1]
            n2 = 1 if i == n - 1 else suffix[i + 1]
            result.append(n1 * n2)

        return result


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test with all positive integers."""
    assert sln.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_002(sln):
    """Test with negative numbers and zero."""
    assert sln.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
