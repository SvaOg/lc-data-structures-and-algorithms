"""
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b such that v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b, or any child of a is an ancestor of b.

Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences:
The maximum difference is |8-1|=7.

Example 2:
Input: root = [1,null,2,null,0,3]
Output: 3

Constraints:
- The number of nodes in the tree is in the range [2, 5000].
- 0 <= Node.val <= 10^5
"""

from .treenode import TreeNode
from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        max_diff = 0

        def dfs(node, min_val, max_val):
            nonlocal max_diff
            if not node:
                max_diff = max(max_diff, max_val - min_val)
                return

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            dfs(node.left, min_val, max_val)
            dfs(node.right, min_val, max_val)

        dfs(root, root.val, root.val)

        return max_diff


import pytest


def build_tree(lst):
    return TreeNode.create_from_list(lst)


def test_example_1():
    root = build_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
    # Output: 7
    assert Solution().maxAncestorDiff(root) == 7


def test_example_2():
    root = build_tree([1, None, 2, None, 0, 3])
    # Output: 3
    assert Solution().maxAncestorDiff(root) == 3
