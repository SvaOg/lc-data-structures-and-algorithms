"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

from typing import List
import pytest


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    result = sln.permute(nums)
    assert sorted(result) == sorted(expected)


def test_example_2(sln):
    nums = [0, 1]
    expected = [[0, 1], [1, 0]]
    result = sln.permute(nums)
    assert sorted(result) == sorted(expected)


def test_example_3(sln):
    nums = [1]
    expected = [[1]]
    result = sln.permute(nums)
    assert sorted(result) == sorted(expected)
