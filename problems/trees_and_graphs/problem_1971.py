"""
1971. Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is at most connected by one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are multiple paths between 0 and 2: [0,1,2], [0,2], etc.

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from 0 to 5.

Constraints:
- 1 <= n <= 2 * 10^5
- 0 <= edges.length <= 2 * 10^5
- edges[i].length == 2
- 0 <= ui, vi <= n - 1
- ui != vi
- 0 <= source, destination <= n - 1
- There are no duplicate edges.
- There are no self edges.
"""

from collections import defaultdict
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj_list = [[] for i in range(n)]
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        seen = {source}
        stack = [source]

        while stack:
            curr_v = stack.pop()
            if curr_v == destination:
                return True

            for next_v in adj_list[curr_v]:
                if next_v not in seen:
                    seen.add(next_v)
                    stack.append(next_v)

        return False


import pytest


def test_example1():
    """
    Example 1:
    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true
    """
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    assert Solution().validPath(n, edges, source, destination) == True


def test_example2():
    """
    Example 2:
    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: false
    """
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5
    assert Solution().validPath(n, edges, source, destination) == False
