from typing import List, Optional, TypeVar, Type
from collections import deque

T = TypeVar("T", bound="TreeNode")


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def create_from_list(cls, values: List[int]) -> T:
        if not values:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            if values[i] is not None:  # left child
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] is not None:  # right child
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root
