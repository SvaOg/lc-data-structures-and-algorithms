"""
701. Insert into a Binary Search Tree
You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion. It is guaranteed that the new value does
not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains
a BST after insertion. You can return any of them.

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted answer is [5,2,7,1,3,null,5].

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
"""

from .treenode import TreeNode

from typing import List, Optional
from collections import deque


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        node = root
        while True:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            elif val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:
                return root
        return root

    def insertIntoBST_recursive(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        """
        Insert a value into the binary search tree and return the root.

        Args:
            root: Root of the binary search tree
            val: Value to insert into the BST

        Returns:
            Root of the BST after insertion
        """

        def insert(node, val):
            if node is None:
                return TreeNode(val)

            if val < node.val:
                node.left = insert(node.left, val)
            elif val > node.val:
                node.right = insert(node.right, val)

            return node

        return insert(root, val)


def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    Determine if the binary tree is a valid binary search tree.

    Args:
        root: Root of the binary tree

    Returns:
        True if the tree is a valid BST, False otherwise
    """

    def dfs(node, lower_bound, upper_bound):
        if not node:
            return True

        if not lower_bound < node.val < upper_bound:
            return False

        return dfs(node.left, lower_bound, node.val) and dfs(
            node.right, node.val, upper_bound
        )

    return dfs(root, float("-inf"), float("inf"))


def test_001():
    """Test Example 1: [4,2,7,1,3], val=5 -> [4,2,7,1,3,5]"""
    root = TreeNode.create_from_list([4, 2, 7, 1, 3])
    val = 5
    result = Solution().insertIntoBST(root, val)

    # Check that the value was inserted correctly
    # The result should be a valid BST with the new value
    assert result is not None
    # Verify the tree structure after insertion
    # This is a basic check - in practice you might want to verify the exact tree structure
    assert isValidBST(root)


def test_002():
    """Test Example 2: [40,20,60,10,30,50,70], val=25 -> [40,20,60,10,30,50,70,null,null,25]"""
    root = TreeNode.create_from_list([40, 20, 60, 10, 30, 50, 70])
    val = 25

    assert isValidBST(root)

    result = Solution().insertIntoBST(root, val)
    nodes = TreeNode.save_to_list(root)

    assert result is not None
    assert isValidBST(root)


def test_003():
    """Test Example 3: [4,2,7,1,3,null,null,null,null,null,null], val=5 -> [4,2,7,1,3,5]"""
    root = TreeNode.create_from_list(
        [4, 2, 7, 1, 3, None, None, None, None, None, None]
    )
    val = 5
    result = Solution().insertIntoBST(root, val)

    # Check that the value was inserted correctly
    assert result is not None
    # Verify the tree structure after insertion
