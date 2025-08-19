"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 
Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p1: Optional[TreeNode], q1: Optional[TreeNode]) -> bool:
            if p1 is None and q1 is None:
                return True
            if p1 is None or q1 is None:
                return False
            return (
                p1.val == q1.val and dfs(p1.left, q1.left) and dfs(p1.right, q1.right)
            )

        return dfs(p, q)


def test_001():
    p = TreeNode.create_from_list([1, 2, 3])
    q = TreeNode.create_from_list([1, 2, 3])
    assert Solution().isSameTree(p, q) == True


def test_002():
    p = TreeNode.create_from_list([1, 2])
    q = TreeNode.create_from_list([1, None, 2])
    assert Solution().isSameTree(p, q) == False


def test_003():
    p = TreeNode.create_from_list([1, 2, 1])
    q = TreeNode.create_from_list([1, 1, 2])
    assert Solution().isSameTree(p, q) == False
