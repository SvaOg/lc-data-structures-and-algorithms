"""
113. Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

from .treenode import TreeNode
from typing import List, Optional
import pytest


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(node, path, total):
            if not node:
                return

            path.append(node.val)
            total += node.val

            if total <= targetSum:
                if node.left or node.right:
                    backtrack(node.left, path, total)
                    backtrack(node.right, path, total)
                else:
                    if total == targetSum:
                        result.append(path[:])

            path.pop()

        result = []
        backtrack(root, [], 0)
        return result


@pytest.fixture
def sln():
    yield Solution()


def test_example_1(sln):
    """Test the first example from the problem description."""
    root = TreeNode.create_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    result = sln.pathSum(root, 22)
    expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert len(result) == len(expected)
    for path in expected:
        assert path in result


def test_example_2():
    """Test the second example from the problem description."""
    s = Solution()
    root = TreeNode.create_from_list([1, 2, 3])
    result = s.pathSum(root, 5)
    assert result == []


def test_example_3():
    """Test the third example from the problem description."""
    s = Solution()
    root = TreeNode.create_from_list([1, 2])
    result = s.pathSum(root, 0)
    assert result == []


def test_empty_tree():
    """Test with an empty tree."""
    s = Solution()
    root = TreeNode.create_from_list([])
    result = s.pathSum(root, 0)
    assert result == []


def test_single_node():
    """Test with a single node tree."""
    root = TreeNode.create_from_list([5])
    result = Solution().pathSum(root, 5)
    assert result == [[5]]

    result = Solution().pathSum(root, 10)
    assert result == []


def test_complex_tree():
    """Test with a more complex tree structure."""
    s = Solution()
    root = TreeNode.create_from_list([1, 2, 3, 4, 5, 6, 7])
    result = s.pathSum(root, 7)
    expected = [[1, 2, 4]]
    assert result == expected
