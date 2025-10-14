"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the nodes of the linked list that have Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
- The number of nodes in the list is in the range [0, 10^4].
- 1 <= Node.val <= 50
- 0 <= val <= 50
"""

from typing import Optional
from .linked_lists import (
    ListNode,
    build_linked_list,
    linked_list_to_list,
)
import pytest


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return dummy.next


def test_001():
    head = build_linked_list([1, 2])
    val = 2
    expected = [1]
    result = Solution().removeElements(head, val)
    assert linked_list_to_list(result) == expected


def test_example_1():
    head = build_linked_list([1, 2, 6, 3, 4, 5, 6])
    val = 6
    expected = [1, 2, 3, 4, 5]
    result = Solution().removeElements(head, val)
    assert linked_list_to_list(result) == expected


def test_example_2():
    head = build_linked_list([])
    val = 1
    expected = []
    result = Solution().removeElements(head, val)
    assert linked_list_to_list(result) == expected


def test_example_3():
    head = build_linked_list([7, 7, 7, 7])
    val = 7
    expected = []
    result = Solution().removeElements(head, val)
    assert linked_list_to_list(result) == expected
