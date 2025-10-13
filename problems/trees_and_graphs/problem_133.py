"""
133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph has only one node with val = 1 and it has no neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it has no nodes.

Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

Follow up: Can you clone the graph without using a hash map?
"""

from typing import List, Optional
import pytest


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def create_from_adj_list(adj_list):
    if not adj_list:
        return None

    if len(adj_list) == 1 and len(adj_list[0]) == 0:
        return Node(1)

    vertexes = set()
    for nb in adj_list:
        for v in nb:
            vertexes.add(v)

    nodes = [Node(v) for v in sorted(vertexes)]
    for i, nb in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in nb]

    return nodes[0]


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not Node:
            return None


@pytest.fixture
def sln():
    yield Solution()


from typing import Dict, List


class IntGraphNode:
    def __init__(self, value=0, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []


class Solution1:
    def copy_graph(self, node: IntGraphNode) -> Dict[int, List[int]]:
        def dfs(node):
            if node.value in visited:
                return
            visited.add(node.value)
            adj_list[node.value] == [nd.value for nd in node.neighbors]
            for n in node.neighbors:
                dfs(n)

        adj_list = {}
        visited = set()
        dfs(node)
        return adj_list


def test_001(sln):
    """Test the first example from the problem description."""
    edges = [[2, 4], [1, 3], [2, 4], [1, 3]]

    node1 = create_from_adj_list(edges)
    node2 = node1.neighbors[0]
    node3 = node2.neighbors[1]
    node4 = node1.neighbors[1]

    assert node1.val == 1
    assert node2.val == 2
    assert node3.val == 3
    assert node4.val == 4

    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node4 = Node(4)

    # node1.neighbors = [node2, node4]
    # node2.neighbors = [node1, node3]
    # node3.neighbors = [node2, node4]
    # node4.neighbors = [node1, node3]

    # result = sln.cloneGraph(node1)
    # assert result is not None
    # assert result.val == 1
    # assert len(result.neighbors) == 2
    # assert result.neighbors[0].val == 2
    # assert result.neighbors[1].val == 4


def test_002(sln):
    """Test the second example from the problem description."""
    # Create the graph: [[]] - single node with no neighbors
    node1 = Node(1)
    node1.neighbors = []

    result = sln.cloneGraph(node1)
    assert result is not None
    assert result.val == 1
    assert len(result.neighbors) == 0


def test_003(sln):
    """Test the third example from the problem description."""
    # Create the graph: [] - empty graph
    result = sln.cloneGraph(None)
    assert result is None


def test_004(sln):
    """Test edge case with single node."""
    # Single node with no neighbors
    node1 = Node(1)

    result = sln.cloneGraph(node1)
    assert result is not None
    assert result.val == 1
    assert len(result.neighbors) == 0
    assert result is not node1  # Should be a different object
