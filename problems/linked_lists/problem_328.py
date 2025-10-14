"""
328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
- The number of nodes in the linked list is in the range [0, 10^4].
- -10^6 <= Node.val <= 10^6
"""

from typing import Optional
from .linked_lists import (
    ListNode,
    build_linked_list,
    linked_list_to_list,
)
import pytest


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_odd, dummy_even = ListNode(0), ListNode(0)

        pos_odd, pos_even = dummy_odd, dummy_even
        curr = head
        counter = 1

        while curr:
            next = curr.next

            if counter % 2:
                pos_odd.next = curr
                pos_odd = curr
            else:
                pos_even.next = curr
                pos_even = curr

            curr = next
            counter += 1

        pos_even.next = None
        pos_odd.next = dummy_even.next
        return dummy_odd.next


def test_example_1():
    head = build_linked_list([1, 2, 3, 4, 5])
    expected = [1, 3, 5, 2, 4]
    result = Solution().oddEvenList(head)
    assert linked_list_to_list(result) == expected


def test_example_2():
    head = build_linked_list([2, 1, 3, 5, 6, 4, 7])
    expected = [2, 3, 6, 7, 1, 5, 4]
    result = Solution().oddEvenList(head)
    assert linked_list_to_list(result) == expected
