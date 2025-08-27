"""
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if the binary tree is a valid binary search tree.

        Args:
            root: Root of the binary tree

        Returns:
            True if the tree is a valid BST, False otherwise
        """

        def dfs(node, lower_bound, upper_bound):
            if not node:
                return True

            if not lower_bound < node.val < upper_bound:
                return False

            return dfs(node.left, lower_bound, node.val) and dfs(
                node.right, node.val, upper_bound
            )

        return dfs(root, float("-inf"), float("inf"))


def test_001():
    """Test Example 1: [2,1,3] -> true"""
    root = TreeNode.create_from_list([2, 1, 3])
    result = Solution().isValidBST(root)
    expected = True
    assert result == expected, f"Expected {expected}, but got {result}"


def test_002():
    """Test Example 2: [5,1,4,null,null,3,6] -> false"""
    root = TreeNode.create_from_list([5, 1, 4, None, None, 3, 6])
    result = Solution().isValidBST(root)
    expected = False
    assert result == expected, f"Expected {expected}, but got {result}"
