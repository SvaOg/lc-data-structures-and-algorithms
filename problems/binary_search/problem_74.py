"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write an algorithm with O(log(m * n)) runtime complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
Each row of matrix is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
"""

from typing import List
import pytest


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_value(idx):
            i = idx // n
            j = idx % n
            return matrix[i][j]

        m, n = len(matrix), len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            value = get_value(mid)
            if value == target:
                return True
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Example 1: target exists in the matrix."""
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert sln.searchMatrix(matrix, target) is True


def test_002(sln):
    """Example 2: target does not exist in the matrix."""
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert sln.searchMatrix(matrix, target) is False
