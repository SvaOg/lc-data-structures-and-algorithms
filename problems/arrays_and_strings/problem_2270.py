"""
2270. Number of Ways to Split Array

You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

- The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
- There is at least one element to the right of i. That is, 0 <= i < n - 1.

Return the number of valid splits in nums.

Example 1:
Input: nums = [10,4,-8,7]
Output: 2
Explanation:
There are three ways of splitting nums into two non-empty parts:
- Split at index 0. The first part is [10], and the second part is [4,-8,7]. The sum of the first part is 10, and the sum of the second part is 3. Since 10 >= 3, this is a valid split.
- Split at index 1. The first part is [10,4], and the second part is [-8,7]. The sum of the first part is 14, and the sum of the second part is -1. Since 14 >= -1, this is a valid split.
- Split at index 2. The first part is [10,4,-8], and the second part is [7]. The sum of the first part is 6, and the sum of the second part is 7. Since 6 < 7, this is not a valid split.
Thus, the number of valid splits in nums is 2.

Example 2:
Input: nums = [2,3,1,0]
Output: 2
Explanation:
There are three ways of splitting nums into two non-empty parts:
- Split at index 0. The first part is [2], and the second part is [3,1,0]. The sum of the first part is 2, and the sum of the second part is 4. Since 2 < 4, this is not a valid split.
- Split at index 1. The first part is [2,3], and the second part is [1,0]. The sum of the first part is 5, and the sum of the second part is 1. Since 5 >= 1, this is a valid split.
- Split at index 2. The first part is [2,3,1], and the second part is [0]. The sum of the first part is 6, and the sum of the second part is 0. Since 6 >= 0, this is a valid split.
Thus, the number of valid splits in nums is 2.

Constraints:
- 2 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        ans, left_section = 0, 0
        for i in range(len(nums) - 1):
            left_section += nums[i]
            if left_section >= total - left_section:
                ans += 1
        return ans


def test_001():
    sol = Solution()
    # Example 1
    nums1 = [10, 4, -8, 7]
    expected1 = 2
    assert sol.waysToSplitArray(nums1) == expected1


def test_002():
    sol = Solution()
    # Example 2
    nums2 = [2, 3, 1, 0]
    expected2 = 2
    assert sol.waysToSplitArray(nums2) == expected2
