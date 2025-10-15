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
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        pass


def test_001():
    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    assert Solution().minReorder(n, connections) == 3

def test_002():
    n = 5
    connections = [[1,0],[1,2],[3,2],[3,4]]
    assert Solution().minReorder(n, connections) == 2

def test_003():
    n = 3
    connections = [[1,0],[2,0]]
    assert Solution().minReorder(n, connections) == 0
