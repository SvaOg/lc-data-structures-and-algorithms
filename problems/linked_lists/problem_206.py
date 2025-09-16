"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from typing import Optional, List
import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseNode(curr, prev):
            if not curr:
                return prev

            next_node = curr.next
            curr.next = prev

            return reverseNode(next_node, curr)

        return reverseNode(head, None)

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node


# Helper functions for testing
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def test_example_1():
    # Input: head = [1,2,3,4,5]
    # Output: [5,4,3,2,1]
    head = build_linked_list([1, 2, 3, 4, 5])
    result = Solution().reverseList(head)
    assert linked_list_to_list(result) == [5, 4, 3, 2, 1]


def test_example_2():
    # Input: head = [1,2]
    # Output: [2,1]
    head = build_linked_list([1, 2])
    result = Solution().reverseList(head)
    assert linked_list_to_list(result) == [2, 1]


def test_example_3():
    # Input: head = []
    # Output: []
    head = build_linked_list([])
    result = Solution().reverseList(head)
    assert linked_list_to_list(result) == []
