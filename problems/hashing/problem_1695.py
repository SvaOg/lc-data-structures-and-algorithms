"""
1695. Maximum Erasure Value
https://leetcode.com/problems/maximum-erasure-value/

You are given an array of positive integers nums. You must choose a subarray (contiguous elements) with all distinct elements and the maximum possible sum.

Return the maximum possible sum of a subarray with all distinct elements.

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray is [2,4,5,6].

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray is [5,2,1] or [1,2,5].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0

        pos = {}
        start = curr_sum = 0

        for end, num in enumerate(nums):
            curr_sum += num
            previous_pos = pos.get(num, -1)

            while start <= previous_pos:
                curr_sum -= nums[start]
                start += 1

            pos[num] = end
            res = max(res, curr_sum)

        return res

    def maximumUniqueSubarray2(self, nums: List[int]) -> int:
        res = 0

        uniques = set()
        start = curr_sum = 0

        for end, num in enumerate(nums):
            curr_sum += num

            while start < end and num in uniques:
                curr_sum -= nums[start]
                uniques.remove(nums[start])
                start += 1

            uniques.add(num)
            res = max(res, curr_sum)

        return res


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    nums = [4, 2, 4, 5, 6]
    assert solution.maximumUniqueSubarray(nums) == 17


def test_example_2(solution):
    nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    assert solution.maximumUniqueSubarray(nums) == 8
