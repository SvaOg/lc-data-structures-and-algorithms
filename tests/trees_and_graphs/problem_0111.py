"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_depth = None

        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()

            if not node.left and not node.right:
                if min_depth is None:
                    min_depth = depth
                else:
                    min_depth = min(min_depth, depth)

            if min_depth is not None and depth > min_depth:
                continue
            else:
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))

        return min_depth


def test_001():
    root = TreeNode.create_from_list([3, 9, 20, None, None, 15, 7])
    assert Solution().minDepth(root) == 2


def test_002():
    root = TreeNode.create_from_list([2, None, 3, None, 4, None, 5, None, 6])
    assert Solution().minDepth(root) == 5


def test_003():
    root = None
    assert Solution().minDepth(root) == 0
