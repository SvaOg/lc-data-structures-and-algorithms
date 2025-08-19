"""
1302. Deepest Leaves Sum

Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Explanation: The deepest leaves are nodes with values 7 and 8, and their sum is 15.

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
Explanation: The deepest leaves are nodes with values 9, 1, 4, and 5, and their sum is 19.

Constraints:
The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""

from .treenode import TreeNode
from typing import Optional
from collections import deque


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        deepest_leaves_sum = 0

        queue = deque([root])
        while queue:
            nodes_in_current_level = len(queue)

            current_leaves_sum = 0

            for _ in range(nodes_in_current_level):
                node = queue.popleft()

                if not node.left and not node.right:
                    current_leaves_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            deepest_leaves_sum = current_leaves_sum

        return deepest_leaves_sum


def test_001():
    root = TreeNode.create_from_list(
        [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
    )
    assert Solution().deepestLeavesSum(root) == 15


def test_002():
    root = TreeNode.create_from_list(
        [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
    )
    assert Solution().deepestLeavesSum(root) == 19


def test_003():
    root = TreeNode.create_from_list([1])
    assert Solution().deepestLeavesSum(root) == 1
