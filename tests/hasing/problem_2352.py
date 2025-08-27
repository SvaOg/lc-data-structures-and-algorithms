"""2352. Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/

Given an n x n matrix grid, return the number of pairs (R, C) where the row R and column C are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:
* n == grid.length == grid[i].length
* 1 <= n <= 200
* 1 <= grid[i][j] <= 10^5
"""

from collections import defaultdict
from typing import List
import pytest


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0

        dic = defaultdict(int)
        for r in grid:
            dic[tuple(r)] += 1

        for c in range(len(grid)):
            col = [grid[j][c] for j in range(len(grid))]
            ans += dic[tuple(col)]

        return ans


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1


def test_example_2(solution):
    assert (
        solution.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
        == 3
    )


def test_single_element(solution):
    assert solution.equalPairs([[1]]) == 1


def test_no_matches(solution):
    assert solution.equalPairs([[1, 2], [3, 4]]) == 0


def test_all_same(solution):
    assert solution.equalPairs([[1, 1], [1, 1]]) == 4
