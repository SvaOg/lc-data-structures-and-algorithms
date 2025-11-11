"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: 4

Example 2:
Input: nums = [2, 7, 9, 3, 1]
Output: 12

Example 3:
Input: nums = [2, 1, 1, 2]
Output: 4

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List
import pytest


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Don't try to use setdefault, since its arguments are always calculated before the call
        """

        def dp(index):
            if index < 0:
                # Base case
                return 0

            # Recurrence relation + memoization
            if index not in memo:
                memo[index] = max(dp(index - 2) + nums[index], dp(index - 1))

            return memo[index]

        memo = {}
        return dp(len(nums) - 1)


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    nums = [1, 2, 3, 1]
    assert sln.rob(nums) == 4


def test_002(sln):
    """Test the second example from the problem description."""
    nums = [2, 7, 9, 3, 1]
    assert sln.rob(nums) == 12


def test_003(sln):
    """Test the third example from the problem description."""
    nums = [2, 1, 1, 2]
    assert sln.rob(nums) == 4
