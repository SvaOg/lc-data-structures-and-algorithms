"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from .treenode import TreeNode
from typing import List, Optional
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_side_view = []

        queue = deque([root])
        while queue:
            nodes_in_current_level = len(queue)

            right_side_view.append(queue[-1].val)

            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_side_view


def test_001():
    root = TreeNode.create_from_list([1, 2, 3, None, 5, None, 4])
    assert Solution().rightSideView(root) == [1, 3, 4]


def test_002():
    root = TreeNode.create_from_list([1, 2, 3, 4, None, None, None, 5])
    assert Solution().rightSideView(root) == [1, 3, 4, 5]


def test_003():
    root = TreeNode.create_from_list([1, None, 3])
    assert Solution().rightSideView(root) == [1, 3]


def test_004():
    root = TreeNode.create_from_list([])
    assert Solution().rightSideView(root) == []
