"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100
"""

from .treenode import TreeNode
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def depth(node):
            nonlocal max_diameter

            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            max_diameter = max(max_diameter, left + right)

            return 1 + max(left, right)

        depth(root)

        return max_diameter


import pytest


def build_tree(lst):
    return TreeNode.create_from_list(lst)


def test_001():
    root = build_tree([1, 2, 3, 4, 5])
    assert Solution().diameterOfBinaryTree(root) == 3


def test_example_1():
    root = build_tree([1, 2, 3, 4, 5])
    assert Solution().diameterOfBinaryTree(root) == 3


def test_example_2():
    root = build_tree([1, 2])
    assert Solution().diameterOfBinaryTree(root) == 1
