"""
1496. Path Crossing
https://leetcode.com/problems/path-crossing/

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: The path visits (0, 0) twice.

Constraints:
- 1 <= path.length <= 10^4
- path[i] is either 'N', 'S', 'E', or 'W'.
"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set([(0, 0)])

        for ch in path:
            match ch:
                case "N":
                    y += 1
                case "S":
                    y -= 1
                case "E":
                    x += 1
                case "W":
                    x -= 1
            pos = (x, y)
            if pos in visited:
                return True
            visited.add(pos)
        return False

import pytest

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    path = "NES"
    assert solution.isPathCrossing(path) == False

def test_example_2(solution):
    path = "NESWW"
    assert solution.isPathCrossing(path) == True
