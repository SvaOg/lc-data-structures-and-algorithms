"""
515. Find Largest Value in Each Tree Row
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
"""

from .treenode import TreeNode
from typing import List, Optional
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []

        queue = deque([root])
        while queue:
            nodes_in_current_level = len(queue)

            level_max_value = queue[0].val
            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                level_max_value = max(level_max_value, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level_max_value)

        return ans


def test_001():
    root = TreeNode.create_from_list([1, 3, 2, 5, 3, None, 9])
    assert Solution().largestValues(root) == [1, 3, 9]


def test_002():
    root = TreeNode.create_from_list([1, 2, 3])
    assert Solution().largestValues(root) == [1, 3]


def test_003():
    root = TreeNode.create_from_list([])
    assert Solution().largestValues(root) == []
