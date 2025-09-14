"""
1512. Number of Good Pairs
https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (1,5), and (3,4).

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array is a good pair.

Example 3:
Input: nums = [1,2,3]
Output: 0

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for fr in Counter(nums).values():
            if fr > 1:
                ans += fr * (fr - 1) // 2
        return ans


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    nums = [1, 2, 3, 1, 1, 3]
    assert solution.numIdenticalPairs(nums) == 4


def test_example_2(solution):
    nums = [1, 1, 1, 1]
    assert solution.numIdenticalPairs(nums) == 6


def test_example_3(solution):
    nums = [1, 2, 3]
    assert solution.numIdenticalPairs(nums) == 0
