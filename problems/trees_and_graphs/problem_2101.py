"""
2101. Detonate the Maximum Bombs

You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. A bomb is represented by a 0-indexed integer array bombs[i] = [xi, yi, ri] where xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb detonates, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their range.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Example 1:
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, the left bomb will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

Example 2:
Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation: Detonating either bomb will not detonate the other.

Example 3:
Input: bombs = [[1,2,3],[2,3,1],[3,4,1],[4,5,1],[5,6,1]]
Output: 5
Explanation:
The best sequence is to detonate the 0th bomb, which will detonate the 1st, which will detonate the 2nd, which will detonate the 3rd, which will detonate the 4th.
Thus, all 5 bombs will be detonated.
"""

from collections import defaultdict, deque


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        def dist_squared(x1, y1, x2, y2):
            return (x2 - x1) ** 2 + (y2 - y1) ** 2

        n = len(bombs)
        graph = defaultdict(list)

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, n):
                x2, y2, r2 = bombs[j]
                dist = dist_squared(x1, y1, x2, y2)
                if dist <= r1 * r1:
                    graph[i].append(j)
                if dist <= r2 * r2:
                    graph[j].append(i)

        ans = 0

        for start in range(n):
            stack = [start]
            triggered = set([start])
            cluster_size = 0

            while stack:
                node = stack.pop()
                cluster_size += 1

                for neighbor in graph[node]:
                    if neighbor not in triggered:
                        triggered.add(neighbor)
                        stack.append(neighbor)

            ans = max(ans, cluster_size)

        return ans


import pytest


@pytest.mark.parametrize(
    "bombs, expected",
    [
        ([[2, 1, 3], [6, 1, 4]], 2),  # Example 1
    ],
)
def test_example1(bombs, expected):
    assert Solution().maximumDetonation(bombs) == expected


@pytest.mark.parametrize(
    "bombs, expected",
    [
        ([[1, 1, 5], [10, 10, 5]], 1),  # Example 2
    ],
)
def test_example2(bombs, expected):
    assert Solution().maximumDetonation(bombs) == expected


@pytest.mark.parametrize(
    "bombs, expected",
    [
        ([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], 5),  # Example 3
    ],
)
def test_example3(bombs, expected):
    assert Solution().maximumDetonation(bombs) == expected
