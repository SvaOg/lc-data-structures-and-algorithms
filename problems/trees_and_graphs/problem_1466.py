"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network forms a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

The roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in city 0 and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges [0,1], [1,3], [4,5] to get the final graph where each city can reach city 0.

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges [1,2], [3,2] to get the final graph where each city can reach city 0.

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
"""

from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        seen = set([0])

        def dfs(node_idx):
            nonlocal ans, seen
            for neighbor_idx, edge in graph[node_idx]:
                if neighbor_idx in seen:
                    continue
                if edge[0] == node_idx:
                    ans += 1
                seen.add(neighbor_idx)
                dfs(neighbor_idx)

        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append((y, (x, y)))
            graph[y].append((x, (x, y)))

        dfs(0)

        return ans

    def minReorder1(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node_idx):
            nonlocal ans
            for neighbor_idx in graph[node_idx]:
                if neighbor_idx in seen:
                    continue
                away_edge = (node_idx, neighbor_idx)
                if away_edge in connections:
                    ans += 1
                seen.add(neighbor_idx)
                dfs(neighbor_idx)

        connections = set((x, y) for x, y in connections)

        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        ans = 0
        seen = set([0])
        dfs(0)

        return ans


def test_001():
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    assert Solution().minReorder(n, connections) == 3


def test_002():
    n = 5
    connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
    assert Solution().minReorder(n, connections) == 2


def test_003():
    n = 3
    connections = [[1, 0], [2, 0]]
    assert Solution().minReorder(n, connections) == 0
