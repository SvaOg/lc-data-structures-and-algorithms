"""
LeetCode Problem 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-4| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-7| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] has the maximum size, and the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 0 <= limit <= 10^9
"""

from collections import deque
from typing import List
import pytest


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0

        left, decreasing, increasing = 0, deque(), deque()

        for right, val in enumerate(nums):
            while decreasing and decreasing[-1] < val:
                decreasing.pop()
            decreasing.append(val)

            while increasing and increasing[-1] > val:
                increasing.pop()
            increasing.append(val)

            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans

    def longestSubarray1(self, nums: List[int], limit: int) -> int:
        max_len = 0

        deq_max, deq_min = deque(), deque()

        left = 0
        for right in range(len(nums)):
            while deq_min and nums[deq_min[-1]] >= nums[right]:
                deq_min.pop()
            deq_min.append(right)

            while deq_max and nums[deq_max[-1]] <= nums[right]:
                deq_max.pop()
            deq_max.append(right)

            while True:
                curr_min = nums[deq_min[0]]
                curr_max = nums[deq_max[0]]

                if curr_max - curr_min > limit:
                    left += 1
                    if deq_min[0] < left:
                        deq_min.popleft()
                    if deq_max[0] < left:
                        deq_max.popleft()
                else:
                    break

            max_len = max(max_len, right - left + 1)

        return max_len

    def longestSubarray_bf(self, nums: List[int], limit: int) -> int:
        def is_good(left, right):
            subarr = nums[left : right + 1]
            return max(subarr) - min(subarr) <= limit

        max_len = 0

        left = 0
        for right in range(len(nums)):
            while not is_good(left, right):
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """
    Example 1: General case with limit 4
    """
    nums = [8, 2, 4, 7]
    limit = 4
    expected = 2
    assert sln.longestSubarray(nums, limit) == expected


def test_002(sln):
    """
    Example 2: Subarray with max diff exactly equal to limit
    """
    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    expected = 4
    assert sln.longestSubarray(nums, limit) == expected


def test_003(sln):
    """
    Example 3: Limit is zero, so only consecutive equal elements allowed
    """
    nums = [4, 2, 2, 2, 4, 4, 2, 2]
    limit = 0
    expected = 3
    assert sln.longestSubarray(nums, limit) == expected
