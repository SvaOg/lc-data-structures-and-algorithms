"""
2958. Length of Longest Subarray With at Most K Frequency
https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

Given an integer array nums and an integer k, return the length of the longest subarray that contains at most k occurrences of each element.

Example 1:
Input: nums = [1,2,3,1,2,3,1,2], k = 2
Output: 6
Explanation: The longest subarray is [2,3,1,2,3,1] or [3,1,2,3,1,2], both have length 6 and each element appears at most twice.

Example 2:
Input: nums = [1,2,1,2,1,2,1,2], k = 1
Output: 2
Explanation: The longest subarray is [1,2] or [2,1], both have length 2 and each element appears at most once.

Example 3:
Input: nums = [5,5,5,5,5], k = 2
Output: 2
Explanation: The longest subarray is [5,5] with length 2.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        chars_with_freq_over_k = 0
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            if freq[nums[right]] == k + 1:
                chars_with_freq_over_k += 1

            if chars_with_freq_over_k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == k:
                    chars_with_freq_over_k -= 1
                left += 1

        return len(nums) - left

    def maxSubarrayLength2(self, nums: List[int], k: int) -> int:
        max_len = 0
        left = 0
        freq = defaultdict(int)
        for right in range(len(nums)):
            num = nums[right]
            freq[num] += 1
            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    nums = [1, 2, 3, 1, 2, 3, 1, 2]
    k = 2
    assert solution.maxSubarrayLength(nums, k) == 6


def test_example_2(solution):
    nums = [1, 2, 1, 2, 1, 2, 1, 2]
    k = 1
    assert solution.maxSubarrayLength(nums, k) == 2


def test_example_3(solution):
    nums = [5, 5, 5, 5, 5]
    k = 2
    assert solution.maxSubarrayLength(nums, k) == 2
