"""
930. Binary Subarrays With Sum
https://leetcode.com/problems/binary-subarrays-with-sum/

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:
- 1 <= nums.length <= 3 * 10^4
- nums[i] is either 0 or 1.
- 0 <= goal <= nums.length
"""

import pytest
from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        curr_sum = prefix_zeroes = start = 0

        for end, num in enumerate(nums):
            curr_sum += num

            while start < end and (nums[start] == 0 or curr_sum > goal):
                prefix_zeroes = 0 if nums[start] else prefix_zeroes + 1
                curr_sum -= nums[start]
                start += 1

            if curr_sum == goal:
                res += 1 + prefix_zeroes

        return res

    def numSubarraysWithSum1(self, nums: List[int], goal: int) -> int:
        ans = 0
        curr_sum = 0
        freq = defaultdict(int)
        freq[0] = 1
        for end in range(len(nums)):
            curr_sum += nums[end]
            delta = curr_sum - goal
            ans += freq[delta]
            freq[curr_sum] += 1
        return ans


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    nums = [1, 0, 1, 0, 1]
    goal = 2
    assert solution.numSubarraysWithSum(nums, goal) == 4


def test_example_2(solution):
    nums = [0, 0, 0, 0, 0]
    goal = 0
    assert solution.numSubarraysWithSum(nums, goal) == 15
