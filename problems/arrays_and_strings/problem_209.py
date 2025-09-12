"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

Problem link: https://leetcode.com/problems/minimum-size-subarray-sum/
"""

from typing import List
import pytest


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        left = 0
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return res if res != float("inf") else 0

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        curr_sum = nums[0]
        if curr_sum >= target:
            return 1

        answer = 0

        p1, p2, n = 0, 0, len(nums)

        while True:
            while curr_sum < target:
                p2 += 1
                if p2 == n:
                    return answer
                curr_sum += nums[p2]

            while curr_sum >= target and p1 <= p2:
                if not answer:
                    answer = p2 - p1 + 1
                else:
                    answer = min(answer, p2 - p1 + 1)

                curr_sum -= nums[p1]
                p1 += 1

        return answer


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    expected = 2
    assert sln.minSubArrayLen(target, nums) == expected


def test_example_2(sln):
    target = 4
    nums = [1, 4, 4]
    expected = 1
    assert sln.minSubArrayLen(target, nums) == expected


def test_example_3(sln):
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    expected = 0
    assert sln.minSubArrayLen(target, nums) == expected
