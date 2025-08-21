"""
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000"""

from .treenode import TreeNode
from typing import List, Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )


def test_example_1():
    s = Solution()
    root = TreeNode.create_from_list([5,4,8,11,None,13,4,7,2,None,None,None,1])
    assert s.hasPathSum(root, 22) == True

def test_example_2():
    s = Solution()
    root = TreeNode.create_from_list([1,2,3])
    assert s.hasPathSum(root, 5) == False

def test_example_3():
    s = Solution()
    root = TreeNode.create_from_list([])
    assert s.hasPathSum(root, 0) == False

