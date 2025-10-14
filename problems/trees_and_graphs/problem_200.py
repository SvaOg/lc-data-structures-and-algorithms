"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == "1"

        def dfs(start_row, start_col):
            stack = [(start_row, start_col)]
            while stack:
                row, col = stack.pop()
                for dx, dy in directions:
                    next_row, next_col = row + dx, col + dy
                    if is_valid(next_row, next_col):
                        grid[next_row][next_col] = "0"
                        stack.append((next_row, next_col))

        n, m = len(grid), len(grid[0])
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid[i][j] == "0"
                    ans += 1
                    dfs(i, j)

        return ans

    def numIslands_iteractive(self, grid: List[List[str]]) -> int:
        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == "1"

        def dfs(start_row, start_col):
            stack = [(start_row, start_col)]
            while stack:
                row, col = stack.pop()
                for dx, dy in directions:
                    next_row, next_col = row + dx, col + dy
                    if (
                        is_valid(next_row, next_col)
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))

        n, m = len(grid), len(grid[0])
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        ans = 0

        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    ans += 1
                    dfs(i, j)

        return ans

    def numIslands_recursive(self, grid: List[List[str]]) -> int:
        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == "1"

        def dfs(row, col):
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if is_valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        n, m = len(grid), len(grid[0])
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        ans = 0

        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    ans += 1
                    dfs(i, j)

        return ans


def test_example_1():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    expected = 1
    assert Solution().numIslands(grid) == expected


def test_example_2():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    expected = 3
    assert Solution().numIslands(grid) == expected
