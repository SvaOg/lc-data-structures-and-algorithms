"""
977. Squares of a Sorted Array

This script provides a template for working on LeetCode problem 977.

Problem link: https://leetcode.com/problems/squares-of-a-sorted-array/
"""

from typing import List
import pytest


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

        :param nums: List[int] - The input array sorted in non-decreasing order.
        :return: List[int] - The sorted array of squares.
        """
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                v = nums[left]
                left += 1
            else:
                v = nums[right]
                right -= 1
            result[i] = v * v

        return result


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    nums = [-4, -1, 0, 3, 10]
    expected = [0, 1, 9, 16, 100]
    result = sln.sortedSquares(nums)
    assert result == expected


def test_example_2(sln):
    nums = [-7, -3, 2, 3, 11]
    expected = [4, 9, 9, 49, 121]
    result = sln.sortedSquares(nums)
    assert result == expected


def test_empty(sln):
    nums = []
    expected = []
    result = sln.sortedSquares(nums)
    assert result == expected


def test_single_element(sln):
    nums = [5]
    expected = [25]
    result = sln.sortedSquares(nums)
    assert result == expected
