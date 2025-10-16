"""
863. All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []

Example 3:
Input: root = [0,1,null,3,2], target = 2, k = 1
Output: [3]

Constraints:
- The number of nodes in the tree is in the range [1, 500].
- 0 <= Node.val <= 500
- All the values Node.val are unique.
- target is the value of one of the nodes in the tree.
- 0 <= k <= 1000
"""

from collections import defaultdict, deque
from typing import Optional, List
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceK(
        self, root: Optional[TreeNode], target: TreeNode, k: int
    ) -> List[int]:
        graph = defaultdict(list)

        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                stack.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)

        seen = {target.val}
        queue = [target.val]
        level = 0

        while queue and level <= k:
            curr_level_count = len(queue)
            if level == k:
                return queue
            else:
                for _ in range(curr_level_count):
                    curr_node = queue[0]
                    queue = queue[1:]
                    for next_node in graph[curr_node]:
                        if next_node not in seen:
                            seen.add(next_node)
                            queue.append(next_node)
            level += 1

        return []


def _make_tree(lst, target_val):
    """
    Helper to make TreeNode from list representation (LeetCode style).
    Returns the root and a dict mapping values to nodes.
    """
    if not lst:
        return None, {}

    nodes = []
    target = None
    for val in lst:
        node = TreeNode(val) if val is not None else None
        nodes.append(node)
        if val == target_val:
            target = node

    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root, target


def test_example_1():
    # root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
    vals = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root, target = _make_tree(vals, 5)
    k = 2
    # Output: [7,4,1]
    result = Solution().distanceK(root, target, k)
    assert set(result) == {7, 4, 1}


def test_example_2():
    # root = [1], target = 1, k = 3
    vals = [1]
    root, target = _make_tree(vals, 1)
    k = 3
    # Output: []
    result = Solution().distanceK(root, target, k)
    assert result == []


def test_example_3():
    # root = [0,1,None,3,2], target = 2, k = 1
    vals = [0, 1, None, 3, 2]
    root, target = _make_tree(vals, 2)
    k = 1
    # Output: [3]
    result = Solution().distanceK(root, target, k)
    assert set(result) == {1}
