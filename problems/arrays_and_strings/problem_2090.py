"""
2090. K Radius Subarray Averages

You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

- For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) // 4 = 11 // 4 = 2.75, which truncates to 2.

Example 1:
Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], avg[2], avg[6], avg[7], and avg[8] are -1 because there are less than k elements before or after them.
- The subarray centered at index 3 is [4,3,9,1,8,5,2] (from index 0 to 6). The average is (4+3+9+1+8+5+2)//7 = 32//7 = 4.
- The subarray centered at index 4 is [3,9,1,8,5,2,6] (from index 1 to 7). The average is (3+9+1+8+5+2+6)//7 = 34//7 = 4.
- The subarray centered at index 5 is [9,1,8,5,2,6] (from index 2 to 8). The average is (9+1+8+5+2+6)//7 = 31//7 = 4.

Example 2:
Input: nums = [100000], k = 0
Output: [100000]
Explanation: The radius k is 0, so the average is the number itself.

Example 3:
Input: nums = [8], k = 100000
Output: [-1]
Explanation: k is larger than the length of nums, so the answer is -1.

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 0 <= nums[i], k <= 10^5

Problem link: https://leetcode.com/problems/k-radius-subarray-averages/
"""

from typing import List
import pytest


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])

        avgs = [-1] * n
        for pos in range(k, n - k):
            left = pos - k
            right = pos + k
            delta = prefix[left - 1] if left else 0
            avgs[pos] = (prefix[right] - delta) // (2 * k + 1)

        return avgs


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k = 3
    expected = [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    assert sln.getAverages(nums, k) == expected


def test_example_2(sln):
    nums = [100000]
    k = 0
    expected = [100000]
    assert sln.getAverages(nums, k) == expected


def test_example_3(sln):
    nums = [8]
    k = 100000
    expected = [-1]
    assert sln.getAverages(nums, k) == expected
