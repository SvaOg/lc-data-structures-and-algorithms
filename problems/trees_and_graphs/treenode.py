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

        items = deque(values)
        root = TreeNode(items.popleft())
        queue = deque([root])

        while queue and items:
            node = queue.popleft()

            left = items.popleft()
            if left is not None:
                node.left = TreeNode(left)
                queue.append(node.left)

            if not items:
                break

            right = items.popleft()
            if right is not None:
                node.right = TreeNode(right)
                queue.append(node.right)

        return root

    @classmethod
    def create_from_list1(cls, values: List[int]) -> T:
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

    @classmethod
    def save_to_list(cls, root: T) -> List[Optional[int]]:
        """
        Convert a binary tree to a list representation.

        Args:
            root: Root node of the binary tree

        Returns:
            List representation of the binary tree with None for empty nodes
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result
