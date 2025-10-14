"""
938. Range Sum of BST
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
"""

from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Return the sum of values of all nodes with a value in the inclusive range [low, high].

        Args:
            root: Root of the binary search tree
            low: Lower bound of the range (inclusive)
            high: Upper bound of the range (inclusive)

        Returns:
            Sum of all node values in the range [low, high]
        """

        if not root:
            return 0

        sum = 0

        stack = [root]
        while stack:
            node = stack.pop()

            if low <= node.val <= high:
                sum += node.val

            if low < node.val and node.left:
                stack.append(node.left)
            if high > node.val and node.right:
                stack.append(node.right)

        return sum


def test_001():
    """Test basic tree structure creation"""
    root = TreeNode.create_from_list([10, 5, 15, 3, 7, None, 18])
    assert root.val == 10
    assert root.left.val == 5
    assert root.right.val == 15
    assert root.left.left.val == 3
    assert root.left.right.val == 7
    assert root.right.right.val == 18


def test_002():
    """Test Example 1: [10,5,15,3,7,null,18], low=7, high=15 -> 32"""
    root = TreeNode.create_from_list([10, 5, 15, 3, 7, None, 18])
    result = Solution().rangeSumBST(root, 7, 15)
    expected = 32  # 7 + 10 + 15
    assert result == expected, f"Expected {expected}, but got {result}"


def test_003():
    """Test Example 2: [10,5,15,3,7,13,18,1,null,6], low=6, high=10 -> 23"""
    root = TreeNode.create_from_list([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    result = Solution().rangeSumBST(root, 6, 10)
    expected = 23  # 6 + 7 + 10
    assert result == expected, f"Expected {expected}, but got {result}"


def test_004():
    """Test single node tree: [5], low=1, high=10 -> 5"""
    root = TreeNode.create_from_list([5])
    result = Solution().rangeSumBST(root, 1, 10)
    expected = 5
    assert result == expected, f"Expected {expected}, but got {result}"


def test_005():
    """Test single node tree outside range: [5], low=10, high=20 -> 0"""
    root = TreeNode.create_from_list([5])
    result = Solution().rangeSumBST(root, 10, 20)
    expected = 0
    assert result == expected, f"Expected {expected}, but got {result}"


def test_006():
    """Test range with only left subtree: [10,5,15,3,7,null,18], low=3, high=7 -> 15"""
    root = TreeNode.create_from_list([10, 5, 15, 3, 7, None, 18])
    result = Solution().rangeSumBST(root, 3, 7)
    expected = 15  # 3 + 5 + 7
    assert result == expected, f"Expected {expected}, but got {result}"


def test_007():
    """Test range with only right subtree: [10,5,15,3,7,null,18], low=15, high=18 -> 33"""
    root = TreeNode.create_from_list([10, 5, 15, 3, 7, None, 18])
    result = Solution().rangeSumBST(root, 15, 18)
    expected = 33  # 15 + 18
    assert result == expected, f"Expected {expected}, but got {result}"


def test_008():
    """Test range covering all nodes: [10,5,15,3,7,null,18], low=1, high=20 -> 58"""
    root = TreeNode.create_from_list([10, 5, 15, 3, 7, None, 18])
    result = Solution().rangeSumBST(root, 1, 20)
    expected = 58  # 3 + 5 + 7 + 10 + 15 + 18
    assert result == expected, f"Expected {expected}, but got {result}"


def test_009():
    """Test range with no nodes: [10,5,15,3,7,null,18], low=20, high=30 -> 0"""
    root = TreeNode.create_from_list([10, 5, 15, 3, 7, None, 18])
    result = Solution().rangeSumBST(root, 20, 30)
    expected = 0
    assert result == expected, f"Expected {expected}, but got {result}"


def test_010():
    """Test complex tree: [10,5,15,3,7,13,18,1,null,6,9], low=4, high=12 -> 25"""
    root = TreeNode.create_from_list([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 9])
    result = Solution().rangeSumBST(root, 4, 12)
    expected = 37  # 5 + 6 + 7 + 9 + 10
    assert result == expected, f"Expected {expected}, but got {result}"
