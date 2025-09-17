"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Follow up: Could you do this in one pass?
"""

from statistics import LinearRegression
from typing import Optional
from src.my_leetcode.linked_lists import (
    ListNode,
    build_linked_list,
    linked_list_to_list,
)
import pytest


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        prev, curr, last = None, head, head
        while n:
            last = last.next
            n -= 1

        while last:
            prev = curr
            curr = curr.next
            last = last.next

        if prev:
            prev.next = curr.next
        else:
            head = head.next

        return head


def test_example_1():
    head = build_linked_list([1, 2, 3, 4, 5])
    n = 2
    expected = [1, 2, 3, 5]
    result = Solution().removeNthFromEnd(head, n)
    assert linked_list_to_list(result) == expected


def test_example_2():
    head = build_linked_list([1])
    n = 1
    expected = []
    result = Solution().removeNthFromEnd(head, n)
    assert linked_list_to_list(result) == expected


def test_example_3():
    head = build_linked_list([1, 2])
    n = 1
    expected = [1]
    result = Solution().removeNthFromEnd(head, n)
    assert linked_list_to_list(result) == expected
