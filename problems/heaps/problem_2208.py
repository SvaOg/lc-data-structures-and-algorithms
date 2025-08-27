"""2208. Minimum Operations to Halve Array Sum
https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)

Return the minimum number of operations to reduce the sum of nums by at least half.

Example 1:
Input: nums = [5,19,8,1]
Output: 3
Explanation: The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33.
The following is one of the ways to reduce the sum by at least half:
Pick the number 19 and reduce it to 9.5.
Pick the number 9.5 and reduce it to 4.75.
Pick the number 8 and reduce it to 4.
The final array is [5, 4.75, 4, 1] with a total sum of 14.75.
The sum has been reduced by 33 - 14.75 = 18.25, which is at least half of the initial sum, 33/2 = 16.5.
Overall, 3 operations were used so we return 3.
It can be shown that we cannot reduce the sum by at least half in less than 3 operations.

Example 2:
Input: nums = [3,8,20]
Output: 3
Explanation: The initial sum of nums is equal to 3 + 8 + 20 = 31.
The following is one of the ways to reduce the sum by at least half:
Pick the number 20 and reduce it to 10.
Pick the number 10 and reduce it to 5.
Pick the number 8 and reduce it to 4.
The final array is [3, 4, 5] with a total sum of 12.
The sum has been reduced by 31 - 12 = 19, which is at least half of the initial sum, 31/2 = 15.5.
Overall, 3 operations were used so we return 3.
It can be shown that we cannot reduce the sum by at least half in less than 3 operations.

Constraints:
* 1 <= nums.length <= 10^5
* 1 <= nums[i] <= 10^7
"""

import heapq
from typing import List
import pytest


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        nums = [-n for n in nums]
        heapq.heapify(nums)

        count = 0
        while target > 0:
            count += 1
            x = heapq.heappop(nums)
            target += x / 2
            heapq.heappush(nums, x / 2)
        return count


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.halveArray([5, 19, 8, 1]) == 3


def test_example_2(solution):
    assert solution.halveArray([3, 8, 20]) == 3


def test_single_element(solution):
    assert solution.halveArray([1]) == 1


def test_all_same(solution):
    assert solution.halveArray([10, 10, 10]) == 3


def test_powers_of_two(solution):
    assert solution.halveArray([1, 2, 4, 8, 16]) == 3
