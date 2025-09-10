"""
LeetCode Problem 1004: Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,1,0,0], k = 0
Output: 3
Explanation: [0,0,1,1,1,0,0]
Since k is 0, you cannot flip any 0's. The longest subarray of 1's is [1,1,1] with length 3.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
- 0 <= k <= nums.length

Problem link: https://leetcode.com/problems/max-consecutive-ones-iii/
"""

from typing import List
import pytest


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Args:
            nums (List[int]): The input binary array.
            k (int): The maximum number of 0's that can be flipped.

        Returns:
            int: The maximum number of consecutive 1's in the array if you can flip at most k 0's.
        """
        left = 0
        curr = 0
        answer = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            answer = max(answer, right - left + 1)

        return answer


@pytest.fixture
def sln():
    yield Solution()


def test_example1(sln):
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    # After flipping two 0's at positions 3 and 4, the longest sequence of 1's is 6.
    assert sln.longestOnes(nums, k) == 6


def test_example2(sln):
    nums = [0, 0, 1, 1, 1, 0, 0]
    k = 0
    # No flips allowed, so the longest sequence of 1's is 3.
    assert sln.longestOnes(nums, k) == 3


def test_all_ones(sln):
    nums = [1, 1, 1, 1, 1]
    k = 1
    # All are already 1's, so the answer is 5.
    assert sln.longestOnes(nums, k) == 5


def test_all_zeros(sln):
    nums = [0, 0, 0, 0]
    k = 2
    # Can flip two 0's, so the answer is 2.
    assert sln.longestOnes(nums, k) == 2


def test_k_equals_length(sln):
    nums = [0, 0, 0, 0]
    k = 4
    # Can flip all 0's, so the answer is 4.
    assert sln.longestOnes(nums, k) == 4
