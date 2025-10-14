"""
530. Minimum Absolute Difference in BST
Given the root of a Binary Search Tree (BST), return the minimum absolute difference
between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1
Explanation: The minimum absolute difference is 1, which is the difference between 2 and 1.

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
Explanation: The minimum absolute difference is 1, which is the difference between 1 and 0.

Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""

from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Return the minimum absolute difference between the values of any two different nodes in the BST.

        Args:
            root: Root of the binary search tree

        Returns:
            Minimum absolute difference between any two node values
        """

        last_val = None
        min_abs_diff = float("inf")

        def inorder_dfs(node):
            nonlocal last_val, min_abs_diff

            if node is None:
                return

            inorder_dfs(node.left)

            if last_val is not None:
                min_abs_diff = min(min_abs_diff, abs(node.val - last_val))
            last_val = node.val

            inorder_dfs(node.right)

        inorder_dfs(root)

        return min_abs_diff


def test_001():
    """Test Example 1: [4,2,6,1,3] -> 1"""
    root = TreeNode.create_from_list([4, 2, 6, 1, 3])
    result = Solution().getMinimumDifference(root)
    expected = 1  # Difference between 2 and 1
    assert result == expected, f"Expected {expected}, but got {result}"


def test_002():
    """Test Example 2: [1,0,48,null,null,12,49] -> 1"""
    root = TreeNode.create_from_list([1, 0, 48, None, None, 12, 49])
    result = Solution().getMinimumDifference(root)
    expected = 1  # Difference between 1 and 0
    assert result == expected, f"Expected {expected}, but got {result}"
