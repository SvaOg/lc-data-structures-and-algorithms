"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""

from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def goodNodes1(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            if node.val >= max_val:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)

    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        stack = [(root, root.val)]
        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                good_nodes += 1
            max_val = max(max_val, node.val)
            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))

        return good_nodes


def test_001():
    root = TreeNode.create_from_list([3, 1, 4, 3, None, 1, 5])
    assert Solution().goodNodes(root) == 4


def test_002():
    root = TreeNode.create_from_list([3, 3, None, 4, 2])
    assert Solution().goodNodes(root) == 3


def test_003():
    root = TreeNode.create_from_list([1])
    assert Solution().goodNodes(root) == 1
