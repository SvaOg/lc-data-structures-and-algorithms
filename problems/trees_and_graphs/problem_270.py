"""
270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/

Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

Assume there is only one unique value in the BST that is closest to the target.

Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^9
- -10^9 <= target <= 10^9
"""

from typing import Optional
from .treenode import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        curr_best_match = None
        curr_delta = float("inf")
        stop = False

        def inorder_dfs(node):
            nonlocal curr_best_match, curr_delta, stop

            if not node or stop:
                return

            inorder_dfs(node.left)

            delta = abs(target - node.val)
            if delta < curr_delta:
                curr_best_match = node.val
                curr_delta = delta
            else:
                stop = True

            inorder_dfs(node.right)

        inorder_dfs(root)
        return curr_best_match


def test_example_1():
    # Input: root = [4,2,5,1,3], target = 3.714286
    root = TreeNode.create_from_list([4, 2, 5, 1, 3])
    target = 3.714286
    expected = 4
    assert Solution().closestValue(root, target) == expected


def test_example_2():
    # Input: root = [1], target = 4.428571
    root = TreeNode.create_from_list([1])
    target = 4.428571
    expected = 1
    assert Solution().closestValue(root, target) == expected
