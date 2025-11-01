"""
0410. Split Array Largest Sum

You are given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays. The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays. The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is 9.

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4
Explanation: There is a way to split it into three subarrays, [1], [4], and [4], where the largest sum among these subarrays is 4.

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)
"""

from typing import List
import pytest


class Solution:
    """
    https://leetcode.com/problems/split-array-largest-sum/description/
    Inverse of 1283 (Split chocolate bar)
    Binary search - pay attention to how divide solution space after match (min/max difference)
    """

    def splitArray(self, nums: List[int], m: int) -> int:
        def check(candidate):
            curr_sum = 0
            num_chunks = 1
            for v in nums:
                if v > candidate:
                    return False
                if curr_sum + v <= candidate:
                    curr_sum += v
                else:
                    num_chunks += 1
                    curr_sum = v
            return num_chunks <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Example 1 from the problem description."""
    nums = [7, 2, 5, 10, 8]
    m = 2
    assert sln.splitArray(nums, m) == 18


def test_002(sln):
    """Example 2 from the problem description."""
    nums = [1, 2, 3, 4, 5]
    m = 2
    assert sln.splitArray(nums, m) == 9


def test_003(sln):
    """Example 3 from the problem description."""
    nums = [1, 4, 4]
    m = 3
    assert sln.splitArray(nums, m) == 4
