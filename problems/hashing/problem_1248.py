"""
LeetCode Problem 1248: Count Number of Nice Subarrays

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice subarrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:
- 1 <= nums.length <= 50000
- 1 <= nums[i] <= 10^5
- 1 <= k <= nums.length
"""

from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1

        ans = curr = 0
        for n in nums:
            curr += n % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans


def test_numberOfSubarrays():
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 2, 1, 1]
    k1 = 3
    expected1 = 2
    assert solution.numberOfSubarrays(nums1, k1) == expected1

    # Test case 2
    nums2 = [2, 4, 6]
    k2 = 1
    expected2 = 0
    assert solution.numberOfSubarrays(nums2, k2) == expected2

    # Test case 3
    nums3 = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k3 = 2
    expected3 = 16
    assert solution.numberOfSubarrays(nums3, k3) == expected3
