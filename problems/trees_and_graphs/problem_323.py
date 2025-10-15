"""
323. Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges.
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        seen = set()
        ans = 0

        for i in range(n):
            if i in seen:
                continue
            ans += 1
            stack = [i]
            seen.add(i)
            while stack:
                curr_node = stack.pop()
                for next_node in graph[curr_node]:
                    if next_node not in seen:
                        seen.add(next_node)
                        stack.append(next_node)

        return ans


import pytest


def test_example1():
    """
    Example 1:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2
    """
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    assert Solution().countComponents(n, edges) == 2


def test_example2():
    """
    Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1
    """
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    assert Solution().countComponents(n, edges) == 1
