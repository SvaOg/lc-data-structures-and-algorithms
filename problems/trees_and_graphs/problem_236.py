"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None

        # first case
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # second case
        if left and right:
            return root

        # third case
        if left:
            return left

        return right


def test_001():
    root = TreeNode.create_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = root.left  # Node with value 5
    q = root.right  # Node with value 1
    result = Solution().lowestCommonAncestor(root, p, q)
    assert result.val == 3


def test_002():
    root = TreeNode.create_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = root.left  # Node with value 5
    q = root.left.right.right  # Node with value 4
    result = Solution().lowestCommonAncestor(root, p, q)
    assert result.val == 5


def test_003():
    root = TreeNode.create_from_list([1, 2])
    p = root  # Node with value 1
    q = root.left  # Node with value 2
    result = Solution().lowestCommonAncestor(root, p, q)
    assert result.val == 1
