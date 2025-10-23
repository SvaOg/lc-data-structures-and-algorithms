"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4
"""

from typing import List
import pytest


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return left


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Example 1: target exists in the array."""
    nums = [1, 3, 5, 6]
    target = 5
    assert sln.searchInsert(nums, target) == 2


def test_002(sln):
    """Example 2: target would be inserted in the middle."""
    nums = [1, 3, 5, 6]
    target = 2
    assert sln.searchInsert(nums, target) == 1


def test_003(sln):
    """Example 3: target greater than all elements (insert at end)."""
    nums = [1, 3, 5, 6]
    target = 7
    assert sln.searchInsert(nums, target) == 4


def test_004(sln):
    """Example 4: target less than all elements (insert at beginning)."""
    nums = [1, 3, 5, 6]
    target = 0
    assert sln.searchInsert(nums, target) == 0
