"""
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""

from typing import Optional, List
from .linked_lists import ListNode, linked_list_to_list, build_linked_list


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        if not head:
            return None

        # Move two pointers until they reach the starting position in the list
        curr, prev = head, None

        while left > 1:
            prev = curr
            curr = curr.next
            left, right = left - 1, right - 1

        # The two pointers that will fix the final connection
        conn, tail = prev, curr

        # Iteratively reverse the nodes until right becomes 0
        while right:
            third = curr.next
            curr.next = prev
            prev, curr = curr, third
            right -= 1

        # Adjust the final connection
        if conn:
            conn.next = prev
        else:
            head = prev

        tail.next = curr

        return head

    def reverseBetween1(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        if not head:
            return None

        left_node = head
        stop = False

        def recurseAndReverse(right_node, m, n):
            nonlocal left_node, stop

            # Base case, don't process any further
            if n == 1:
                return

            right_node = right_node.next

            # Keep moving left pointer until it reaches the position where reversal will begin
            if m > 1:
                left_node = left_node.next

            # Recurse with m and n reduced
            recurseAndReverse(right_node, m - 1, n - 1)

            # Check if we the nodes crossed
            if right_node == left_node or right_node.next == left_node:
                stop = True

            if not stop:
                left_node.val, right_node.val = right_node.val, left_node.val
                left_node = left_node.next

        recurseAndReverse(head, left, right)

        return head

    def reverseBetween2(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        left_node = head
        for i in range(left - 1):
            left_node = left_node.next

        def backtrack(right_node, end):
            nonlocal left_node, stop

            if end == 0:
                return

            backtrack(right_node.next, end - 1)
            if stop:
                return

            if left_node != right_node:
                left_node.val, right_node.val = right_node.val, left_node.val

            if left_node == right_node or left_node.next == right_node:
                stop = True

            left_node = left_node.next

        stop = False
        backtrack(left_node, right - left + 1)

        return head


def test_example_1():
    input = [1, 2, 3, 4, 5]
    left, right = 2, 4
    expected = [1, 4, 3, 2, 5]

    head = build_linked_list(input)
    result = Solution().reverseBetween(head, left, right)
    assert linked_list_to_list(result) == expected


def test_example_1_3():
    input = [1, 2, 3, 4, 5]
    left, right = 4, 5
    expected = [1, 2, 3, 5, 4]

    head = build_linked_list(input)
    result = Solution().reverseBetween(head, left, right)
    assert linked_list_to_list(result) == expected


def test_example_1_1():
    input = [1, 2, 3, 4, 5]
    left, right = 1, 5
    expected = [5, 4, 3, 2, 1]

    head = build_linked_list(input)
    result = Solution().reverseBetween(head, left, right)
    assert linked_list_to_list(result) == expected


def test_example_1_2():
    input = [1, 2, 3, 4, 5]
    left, right = 1, 2
    expected = [2, 1, 3, 4, 5]

    head = build_linked_list(input)
    result = Solution().reverseBetween(head, left, right)
    assert linked_list_to_list(result) == expected


def test_example_2():
    # Input: head = [5], left = 1, right = 1
    # Output: [5]
    head = build_linked_list([5])
    left = 1
    right = 1
    result = Solution().reverseBetween(head, left, right)
    assert linked_list_to_list(result) == [5]


def test_example_3():
    # Input: head = [5], left = 1, right = 1
    # Output: [5]
    head = build_linked_list([3, 4])
    left = 1
    right = 2
    result = Solution().reverseBetween(head, left, right)
    assert linked_list_to_list(result) == [4, 3]
