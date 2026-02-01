"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100
"""

from typing import Optional, List
import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


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
    # Output: [3,4,5]
    head = build_linked_list([1, 2, 3, 4, 5])
    result = Solution().middleNode(head)
    assert linked_list_to_list(result) == [3, 4, 5]


def test_example_2():
    # Input: head = [1,2,3,4,5,6]
    # Output: [4,5,6]
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    result = Solution().middleNode(head)
    assert linked_list_to_list(result) == [4, 5, 6]
