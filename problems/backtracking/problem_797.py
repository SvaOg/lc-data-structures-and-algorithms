"""
797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/description/

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Constraints:
n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i
All the values of graph[i] are unique.
The graph is guaranteed to be a DAG.
"""

from typing import List
import pytest


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(curr):
            node = curr[-1]
            if curr[-1] == n - 1:
                ans.append(curr[:])
                return
            for next_node in graph[node]:
                curr.append(next_node)
                backtrack(curr)
                curr.pop()

        n = len(graph)
        ans = []
        backtrack([0])
        return ans


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    graph = [[1, 2], [3], [3], []]
    expected = [[0, 1, 3], [0, 2, 3]]
    assert sln.allPathsSourceTarget(graph) == expected


def test_002(sln):
    """Test the second example from the problem description."""
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    expected = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    assert sln.allPathsSourceTarget(graph) == expected
