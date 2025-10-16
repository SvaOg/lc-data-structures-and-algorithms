"""
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n, m = len(grid), len(grid[0])

        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == 1

        max_area = 0
        seen = set()

        for row in range(n):
            for col in range(m):
                if not is_valid(row, col) or (row, col) in seen:
                    continue
                area = 1
                stack = [(row, col)]
                seen.add((row, col))
                while stack:
                    x, y = stack.pop()
                    for delta_x, delta_y in directions:
                        next_x, next_y = x + delta_x, y + delta_y
                        if is_valid(next_x, next_y) and (next_x, next_y) not in seen:
                            area += 1
                            seen.add((next_x, next_y))
                            stack.append((next_x, next_y))
                max_area = max(max_area, area)

        return max_area


import pytest


def test_example1():
    """
    Example 1:
    Input: grid = [
      [0,0,1,0,0,0,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,1,1,0,1,0,0,0,0,0,0,0,0],
      [0,1,0,0,1,1,0,0,1,0,1,0,0],
      [0,1,0,0,1,1,0,0,1,1,1,0,0],
      [0,0,0,0,0,0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    Output: 6
    """
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert Solution().maxAreaOfIsland(grid) == 6


def test_example2():
    """
    Example 2:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0
    """
    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert Solution().maxAreaOfIsland(grid) == 0
