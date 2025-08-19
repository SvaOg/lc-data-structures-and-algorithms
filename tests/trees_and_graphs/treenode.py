from typing import List, Optional, TypeVar, Type

T = TypeVar("T", bound="TreeNode")


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def create_from_list(cls, nums: List[int]) -> T:
        if not nums:
            return None
        nodes = [None if v is None else cls(v) for v in nums]
        for i, node in enumerate(nodes):
            if node is not None:
                left_child_index = 2 * i + 1
                node.left = (
                    nodes[left_child_index] if left_child_index < len(nodes) else None
                )
                right_child_index = 2 * i + 2
                node.right = (
                    nodes[right_child_index] if right_child_index < len(nodes) else None
                )
        return nodes[0]
