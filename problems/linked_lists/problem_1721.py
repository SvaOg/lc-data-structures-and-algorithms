"""
1721. Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Example 3:
Input: head = [1], k = 1
Output: [1]

Example 4:
Input: head = [1,2], k = 1
Output: [2,1]

Example 5:
Input: head = [1,2,3], k = 2
Output: [1,2,3]

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 10^5
- 0 <= Node.val <= 100
"""

from typing import Optional
from .linked_lists import (
    ListNode,
    build_linked_list,
    linked_list_to_list,
)
import pytest


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node1, left = head, k
        node2, right = head, k

        curr = head
        while curr:
            curr = curr.next

            if left > 1:
                node1 = node1.next
                left -= 1

            if right > 0:
                right -= 1
            else:
                node2 = node2.next

        node1.val, node2.val = node2.val, node1.val

        return head


def test_example_1():
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 2
    expected = [1, 4, 3, 2, 5]
    result = Solution().swapNodes(head, k)
    assert linked_list_to_list(result) == expected


def test_example_2():
    head = build_linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
    k = 5
    expected = [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
    result = Solution().swapNodes(head, k)
    assert linked_list_to_list(result) == expected


def test_example_3():
    head = build_linked_list([1])
    k = 1
    expected = [1]
    result = Solution().swapNodes(head, k)
    assert linked_list_to_list(result) == expected


def test_example_4():
    head = build_linked_list([1, 2])
    k = 1
    expected = [2, 1]
    result = Solution().swapNodes(head, k)
    assert linked_list_to_list(result) == expected


def test_example_5():
    head = build_linked_list([1, 2, 3])
    k = 2
    expected = [1, 2, 3]
    result = Solution().swapNodes(head, k)
    assert linked_list_to_list(result) == expected
