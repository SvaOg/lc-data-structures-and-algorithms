"""
1129. Shortest Path with Alternating Colors

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is colored either red or blue. You are given two arrays redEdges and blueEdges where:

- redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi.
- blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj.

Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if no such path exists.

Example 1:
--------------------
Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Example 2:
--------------------
Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

Constraints:
- 1 <= n <= 100
- 0 <= redEdges.length, blueEdges.length <= 400
- redEdges[i].length == blueEdges[j].length == 2
- 0 <= ai, bi, uj, vj < n
"""

from collections import defaultdict, deque
from typing import List
import pytest


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:

        RED, BLUE = 0, 1

        red_graph = defaultdict(list)
        for i, j in redEdges:
            red_graph[i].append(j)

        blue_graph = defaultdict(list)
        for i, j in blueEdges:
            blue_graph[i].append(j)

        ans = [float("inf")] * n
        seen = set(((0, RED), (0, BLUE)))
        queue = deque(((0, RED, 0), (0, BLUE, 0)))

        while queue:
            node, color, steps = queue.popleft()
            next_color = BLUE if color == RED else RED
            ans[node] = min(ans[node], steps)

            graph = red_graph if color == RED else blue_graph
            for neighbor in graph[node]:
                if (neighbor, next_color) not in seen:
                    seen.add((neighbor, next_color))
                    queue.append((neighbor, next_color, steps + 1))

        return [x if x != float("inf") else -1 for x in ans]


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    n = 3
    redEdges = [[0, 1], [1, 2]]
    blueEdges = []
    expected = [0, 1, -1]
    assert sln.shortestAlternatingPaths(n, redEdges, blueEdges) == expected


def test_example_2(sln):
    n = 3
    redEdges = [[0, 1]]
    blueEdges = [[2, 1]]
    expected = [0, 1, -1]
    assert sln.shortestAlternatingPaths(n, redEdges, blueEdges) == expected
