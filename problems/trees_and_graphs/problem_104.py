"""
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        ans = 0
        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return ans

    def maxDepth_recursive(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)


def test_001():
    root = TreeNode.create_from_list([3, 9, 20, None, None, 15, 7])
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7


def test_002():
    assert (
        Solution().maxDepth(TreeNode.create_from_list([3, 9, 20, None, None, 15, 7]))
        == 3
    )


def test_003():
    assert Solution().maxDepth(TreeNode.create_from_list([1, None, 2])) == 2
