"""
82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.
"""

from typing import Optional, List
from .linked_lists import (
    ListNode,
    build_linked_list,
    linked_list_to_list,
)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev_node, curr_node = None, head

        while curr_node and curr_node.next:
            if curr_node.val == curr_node.next.val:
                # Found duplicate, need to remove all elements with the same val
                next_node = curr_node.next
                while next_node and next_node.val == curr_node.val:
                    next_node = next_node.next
                if prev_node:
                    prev_node.next, curr_node = next_node, next_node
                else:
                    head, curr_node = next_node, next_node
            else:
                prev_node, curr_node = curr_node, curr_node.next

        return head


def test_001():
    head = build_linked_list([1, 2, 2, 3])
    expected = [1, 3]
    result = Solution().deleteDuplicates(head)
    assert linked_list_to_list(result) == expected


def test_002():
    head = build_linked_list([1, 1, 2, 3])
    expected = [2, 3]
    result = Solution().deleteDuplicates(head)
    assert linked_list_to_list(result) == expected


def test_003():
    head = build_linked_list([1, 2, 3, 3])
    expected = [1, 2]
    result = Solution().deleteDuplicates(head)
    assert linked_list_to_list(result) == expected


def test_example_1():
    head = build_linked_list([1, 2, 3, 3, 4, 4, 5])
    expected = [1, 2, 5]
    result = Solution().deleteDuplicates(head)
    assert linked_list_to_list(result) == expected


def test_example_2():
    head = build_linked_list([1, 1, 1, 2, 3])
    expected = [2, 3]
    result = Solution().deleteDuplicates(head)
    assert linked_list_to_list(result) == expected
