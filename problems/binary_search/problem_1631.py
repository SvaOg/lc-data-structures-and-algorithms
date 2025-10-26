"""
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows - 1, columns - 1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells. This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The path [1,2,3,4,5] has a maximum absolute difference of 1, which is better than any other path.

Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:
m == heights.length
n == heights[i].length
1 <= m, n <= 100
1 <= heights[i][j] <= 10^6
"""

from typing import List
import pytest


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def check(effort):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            seen = {(0, 0)}
            stack = [(0, 0)]

            while stack:
                row, col = stack.pop()
                if (row, col) == (m - 1, n - 1):
                    return True

                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if (
                            abs(heights[next_row][next_col] - heights[row][col])
                            <= effort
                        ):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))

            return False

        m = len(heights)
        n = len(heights[0])
        left = 0
        right = max(max(row) for row in heights)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    assert sln.minimumEffortPath(heights) == 2


def test_002(sln):
    """Test the second example from the problem description."""
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    assert sln.minimumEffortPath(heights) == 1


def test_003(sln):
    """Test the third example from the problem description."""
    heights = [
        [1, 2, 1, 1, 1],
        [1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1],
        [1, 1, 1, 2, 1],
    ]
    assert sln.minimumEffortPath(heights) == 0
