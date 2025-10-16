"""
2368. Reachable Nodes With Restrictions

You are given an integer n representing the number of nodes labeled from 0 to n - 1, a 2D integer array edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi, and an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting any restricted nodes.

Note that node 0 cannot be a restricted node.

Example 1:

Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
Output: 4
Explanation: The diagram above shows the tree. We have the following options:
- Visit node 0
- Visit node 0 -> 1
- Visit node 0 -> 1 -> 2
- Visit node 0 -> 3
Nodes 4 and 5 are restricted so we cannot visit them. We return 4 as the maximum number of nodes we can visit.

Example 2:

Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5,1,6]
Output: 2
Explanation: The diagram above shows the tree. Only nodes 0 and 3 can be visited.

Constraints:
- 2 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- edges represents a valid tree.
- 1 <= restricted.length < n
- 1 <= restricted[i] < n
- All the values of restricted are unique.
- The values of restricted are sorted in strictly increasing order.
"""

from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        restricted = set(restricted)

        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        seen = {0}
        stack = [0]
        while stack:
            curr = stack.pop()
            for next in graph[curr]:
                if next in seen or next in restricted:
                    continue
                seen.add(next)
                stack.append(next)

        return len(seen)


def test_example1():
    """
    Example 1:

    Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
    Output: 4
    """
    n = 7
    edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
    restricted = [4, 5]
    assert Solution().reachableNodes(n, edges, restricted) == 4


def test_example2():
    """
    Example 2:

    Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
    Output: 3
    """
    n = 7
    edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
    restricted = [4, 2, 1]
    output = 3
    assert Solution().reachableNodes(n, edges, restricted) == output
