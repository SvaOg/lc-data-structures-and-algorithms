"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?

Problem link: https://leetcode.com/problems/move-zeroes/
"""

from typing import List
import pytest


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = -1
        for p2 in range(len(nums)):
            if nums[p2]:
                if p1 != -1:
                    nums[p1] = nums[p2]
                    nums[p2] = 0
                    p1 += 1
            else:
                if p1 == -1:
                    p1 = p2


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    sln.moveZeroes(nums)
    assert nums == expected


def test_example_2(sln):
    nums = [0]
    expected = [0]
    sln.moveZeroes(nums)
    assert nums == expected


def test_example_3(sln):
    nums = [2, 1]
    expected = [2, 1]
    sln.moveZeroes(nums)
    assert nums == expected
