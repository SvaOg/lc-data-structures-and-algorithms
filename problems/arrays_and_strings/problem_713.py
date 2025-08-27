"""
713. Subarray Product Less Than K

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]
Note that [10,5,2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
"""

from typing import List
import pytest


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans, left = 0, 0
        curr = 1
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1
        return ans

    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,k,expected",
    [([10, 5, 2, 6], 100, 8), ([1, 2, 3], 0, 0)],
)
def test_numSubarrayProductLessThanK(solution, nums, k, expected):
    assert solution.numSubarrayProductLessThanK(nums, k) == expected
