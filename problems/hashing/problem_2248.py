"""
2248. Intersection of Multiple Arrays
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

Example 1:
Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation:
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

Example 2:
Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation:
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].

Constraints:
1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
"""

from typing import List
import pytest
from collections import defaultdict


class Solution:
    def intersection1(self, nums: List[List[int]]) -> List[int]:
        if not nums:
            return []
        ans = set(nums[0])
        for n in range(1, len(nums)):
            ans = ans.intersection(set(nums[n]))
        return list(sorted(ans))

    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for v in arr:
                counts[v] += 1

        return list(sorted(k for k, v in counts.items() if v == len(nums)))

        if not nums:
            return []
        ans = set(nums[0])
        for n in range(1, len(nums)):
            ans = ans.intersection(set(nums[n]))
        return list(sorted(ans))


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]], [3, 4]),
        ([[1, 2, 3], [4, 5, 6]], []),
    ],
)
def test_intersection(solution, nums, expected):
    assert solution.intersection(nums) == expected
