"""
Problem 542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
--------------------
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
--------------------
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- 1 <= m * n <= 10^4
- mat[i][j] is either 0 or 1.
- There is at least one 0 in mat.
"""

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        queue = deque()
        seen = set()

        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and (row, col) not in seen

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    seen.add((i, j))

        level = 0
        while queue:
            curr_level_items = len(queue)
            level += 1
            for _ in range(curr_level_items):
                curr_row, curr_col = queue.popleft()
                for delta_row, delta_col in directions:
                    next_row, next_col = curr_row + delta_row, curr_col + delta_col
                    if is_valid(next_row, next_col):
                        mat[next_row][next_col] = level
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))

        return mat


def test_example_1():
    input = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    output = Solution().updateMatrix(input)
    assert output == expected


def test_example_2():
    input = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    output = Solution().updateMatrix(input)
    assert output == expected
