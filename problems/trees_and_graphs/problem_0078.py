"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

from typing import List
import pytest


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(curr, i):
            if i > len(nums):
                return

            result.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()

        backtrack([], 0)

        return result


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    nums = [1, 2, 3]
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    result = sln.subsets(nums)
    # Sort both result and expected for comparison since order doesn't matter
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


def test_002(sln):
    """Test the second example from the problem description."""
    nums = [0]
    expected = [[], [0]]
    result = sln.subsets(nums)
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


def test_003(sln):
    """Test edge case with single element."""
    nums = [5]
    expected = [[], [5]]
    result = sln.subsets(nums)
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


def test_004(sln):
    """Test edge case with empty array."""
    nums = []
    expected = [[]]
    result = sln.subsets(nums)
    assert result == expected
