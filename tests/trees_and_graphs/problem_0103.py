"""
103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

from collections import deque
from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return the zigzag level order traversal of binary tree nodes.

        Args:
            root: Root of the binary tree

        Returns:
            List of lists where each inner list represents a level,
            with alternating left-to-right and right-to-left order
        """
        if root is None:
            return []

        answer = []

        queue = deque([root])
        left_to_right = True

        while queue:
            nodes_on_current_level = len(queue)

            start, stop, step = (
                (0, nodes_on_current_level, 1)
                if left_to_right
                else (nodes_on_current_level - 1, -1, -1)
            )
            answer.append([queue[i].val for i in range(start, stop, step)])

            left_to_right = not left_to_right

            for _ in range(nodes_on_current_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return answer


def test_001():
    """Test basic tree structure creation"""
    root = TreeNode.create_from_list([3, 9, 20, None, None, 15, 7])
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7


def test_002():
    """Test Example 1: [3,9,20,null,null,15,7] -> [[3],[20,9],[15,7]]"""
    root = TreeNode.create_from_list([3, 9, 20, None, None, 15, 7])
    expected = [[3], [20, 9], [15, 7]]
    result = Solution().zigzagLevelOrder(root)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_003():
    """Test Example 2: [1] -> [[1]]"""
    root = TreeNode.create_from_list([1])
    expected = [[1]]
    result = Solution().zigzagLevelOrder(root)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_004():
    """Test Example 3: [] -> []"""
    root = TreeNode.create_from_list([])
    expected = []
    result = Solution().zigzagLevelOrder(root)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_005():
    """Test single level with multiple nodes: [1,2,3] -> [[1],[3,2]]"""
    root = TreeNode.create_from_list([1, 2, 3])
    expected = [[1], [3, 2]]
    result = Solution().zigzagLevelOrder(root)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_006():
    """Test deeper tree: [1,2,3,4,5,6,7] -> [[1],[3,2],[4,5,6,7]]"""
    root = TreeNode.create_from_list([1, 2, 3, 4, 5, 6, 7])
    expected = [[1], [3, 2], [4, 5, 6, 7]]
    result = Solution().zigzagLevelOrder(root)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_007():
    """Test tree with None values: [1,2,3,4,None,5,6] -> [[1],[3,2],[4,5,6]]"""
    root = TreeNode.create_from_list([1, 2, 3, 4, None, 5, 6])
    expected = [[1], [3, 2], [4, 5, 6]]
    result = Solution().zigzagLevelOrder(root)
    assert result == expected, f"Expected {expected}, but got {result}"
