"""
1091. Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected (i.e., they are different and share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1.
"""

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = (
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        )

        n, m = len(grid), len(grid[0])

        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == 0

        if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
            return -1

        queue = deque([(0, 0)])
        seen = {(0, 0)}
        level = 1

        while queue:
            curr_level_count = len(queue)
            for _ in range(curr_level_count):
                curr_row, curr_col = queue.popleft()
                if curr_row == n - 1 and curr_col == m - 1:
                    return level

                for dx, dy in directions:
                    next_row, next_col = curr_row + dx, curr_col + dy
                    if (
                        is_valid(next_row, next_col)
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))

            level += 1

        return -1


def test_example_1():
    grid = [[0, 1], [1, 0]]
    expected = 2
    assert Solution().shortestPathBinaryMatrix(grid) == expected


def test_example_2():
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    expected = 4
    assert Solution().shortestPathBinaryMatrix(grid) == expected


def test_example_3():
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    expected = -1
    assert Solution().shortestPathBinaryMatrix(grid) == expected


def test_4():
    grid = [
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
    ]
    expected = 14
    assert Solution().shortestPathBinaryMatrix(grid) == expected
