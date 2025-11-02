"""
78. Subsets
https://leetcode.com/problems/subsets/description/

Editorial:
https://leetcode.com/problems/subsets/editorial/

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
        """
        Solution based on this comment:
        https://leetcode.com/problems/subsets/description/comments/2407981/
        """

        def bit_patterns(num):
            ans = []
            curr_idx = 0
            while num > 0:
                if num & 1:
                    ans.append(curr_idx)
                num = num >> 1
                curr_idx += 1
            return ans

        indexes = [bit_patterns(v) for v in range(2 ** len(nums))]

        ans = []
        for arr in indexes:
            ans.append([nums[i] for i in arr])
        return ans

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking solution from a course
        """

        def backtrack(curr, i):
            if i > len(nums):
                return

            ans.append(curr[:])

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()

        ans = [[]]
        backtrack([], 0)
        return ans

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subset, idx):
            if idx == len(nums):
                result.append(subset[:])
                return
            include = subset[:]
            include.append(nums[idx])
            exclude = subset[:]
            backtrack(include, idx + 1)
            backtrack(exclude, idx + 1)

        result = []
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
