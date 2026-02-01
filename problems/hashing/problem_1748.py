"""
1748. Sum of Unique Elements
https://leetcode.com/problems/sum-of-unique-elements/

You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(v for v, n in Counter(nums).items() if n == 1)


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    nums = [1, 2, 3, 2]
    assert solution.sumOfUnique(nums) == 4


def test_example_2(solution):
    nums = [1, 1, 1, 1, 1]
    assert solution.sumOfUnique(nums) == 0


def test_example_3(solution):
    nums = [1, 2, 3, 4, 5]
    assert solution.sumOfUnique(nums) == 15
