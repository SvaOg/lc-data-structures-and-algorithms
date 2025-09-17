"""
2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

- For n = 1, there is no middle node, so the list becomes empty.

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node at index ⌊7 / 2⌋ = 3 needs to be deleted.
Thus, we return [1,3,4,1,2,6].

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node at index ⌊4 / 2⌋ = 2 needs to be deleted.
Thus, we return [1,2,4].

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node at index ⌊2 / 2⌋ = 1 needs to be deleted.
Thus, we return [2].

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
"""

from typing import Optional
from src.my_leetcode.linked_lists import (
    ListNode,
    build_linked_list,
    linked_list_to_list,
)


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        fast, slow, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head


import pytest


def test_example_1():
    input_list, expected = [1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]
    head = build_linked_list(input_list)
    result = Solution().deleteMiddle(head)
    assert linked_list_to_list(result) == expected


def test_example_1_1():
    input_list, expected = [1, 3, 4, 7, 1, 2, 6, 8], [1, 3, 4, 7, 2, 6, 8]
    head = build_linked_list(input_list)
    result = Solution().deleteMiddle(head)
    assert linked_list_to_list(result) == expected

def test_example_2():
    input_list, expected = [1, 2, 3], [1, 3]
    head = build_linked_list(input_list)
    result = Solution().deleteMiddle(head)
    assert linked_list_to_list(result) == expected

def test_example_2_1():
    input_list, expected = [1, 2, 3, 4], [1, 2, 4]
    head = build_linked_list(input_list)
    result = Solution().deleteMiddle(head)
    assert linked_list_to_list(result) == expected


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),  # Example 1
        ([1, 2, 3, 4], [1, 2, 4]),  # Example 2
        ([2, 1], [2]),  # Example 3
        ([1], []),  # Edge case: single node
    ],
)
def test_delete_middle(input_list, expected):
    head = build_linked_list(input_list)
    result = Solution().deleteMiddle(head)
    assert linked_list_to_list(result) == expected
