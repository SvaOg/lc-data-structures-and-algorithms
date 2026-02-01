from .treenode import TreeNode
from typing import List


def test_001():
    root = TreeNode.create_from_list([3, 9, 20, None, None, 15, 7])
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7


def test_002():
    root = TreeNode.create_from_list([3, 9, 20, None, None, 15, 7])


def test_002():
    pass
