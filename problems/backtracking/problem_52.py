"""
52. N-Queens II
https://leetcode.com/problems/n-queens-ii/description/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
"""

from typing import List
import pytest


class Solution:
    """
    Diagonals have same col-row, anti-diagonals have the same row + col
    """

    def totalNQueens(self, n: int) -> int:
        taken_rows, taken_cols, taken_diags, taken_adiags = set(), set(), set(), set()

        def place_queen(row, col):
            taken_rows.add(row)
            taken_cols.add(col)
            taken_diags.add(row - col)
            taken_adiags.add(row + col)

        def remove_queen(row, col):
            taken_rows.remove(row)
            taken_cols.remove(col)
            taken_diags.remove(row - col)
            taken_adiags.remove(row + col)

        def can_place(row, col):
            return (
                row not in taken_rows
                and col not in taken_cols
                and (row - col) not in taken_diags
                and (row + col) not in taken_adiags
            )

        def backtrack(row):
            nonlocal result
            if row == n:
                result += 1
                return

            for col in range(n):
                queen = (row, col)
                if can_place(*queen):
                    place_queen(*queen)
                    backtrack(row + 1)
                    remove_queen(*queen)

        result = 0
        backtrack(0)
        return result


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    n = 4
    assert sln.totalNQueens(n) == 2


def test_002(sln):
    """Test the second example from the problem description."""
    n = 1
    assert sln.totalNQueens(n) == 1
