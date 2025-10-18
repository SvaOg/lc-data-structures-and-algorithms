"""
1926. Nearest Exit from Entrance in Maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze, except the entrance itself. The exit does not necessarily have to be at the farthest border; it could be at any such accessible cell.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:
-----------
Input: maze = [["+","+",".","+"],
               [".",".",".","+"],
               ["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [0,2] by moving up 1 step.
It is not possible to reach any of the other exits from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
-----------
Input: maze = [["+","+","+"],
               [".",".","."],
               ["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is one exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving right 2 steps.
Thus, the nearest exit is 2 steps away.

Example 3:
-----------
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
"""

from collections import deque
from typing import List
import pytest


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."

        def border(row, col):
            return (
                row == 0
                or row == m - 1
                or col == 0
                or col == n - 1
                and maze[row][col] == "."
            )

        m, n = len(maze), len(maze[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

        queue = deque([(entrance[0], entrance[1], 0)])
        seen = {(entrance[0], entrance[1])}

        while queue:
            row, col, steps = queue.popleft()
            if border(row, col) and steps:
                return steps

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))

        return -1


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]
    expected = 1
    assert sln.nearestExit(maze, entrance) == expected


def test_example_2(sln):
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    expected = 2
    assert sln.nearestExit(maze, entrance) == expected


def test_example_3(sln):
    maze = [[".", "+"]]
    entrance = [0, 0]
    expected = -1
    assert sln.nearestExit(maze, entrance) == expected
