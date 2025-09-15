"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: "ListNode") -> bool:
        if head is None or head.next is None:
            return False

        if head == head.next:
            return True

        slow = head
        fast = slow.next
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next

        return False


import pytest


def build_linked_list_with_cycle(values, pos):
    """
    Helper to build a linked list from values and create a cycle at position pos.
    If pos == -1, no cycle.
    """
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def test_example_1():
    # head = [3,2,0,-4], pos = 1
    head = build_linked_list_with_cycle([3, 2, 0, -4], 1)
    assert Solution().hasCycle(head) == True


def test_example_2():
    # head = [1,2], pos = 0
    head = build_linked_list_with_cycle([1, 2], 0)
    assert Solution().hasCycle(head) == True


def test_example_3():
    # head = [1], pos = -1
    head = build_linked_list_with_cycle([1], -1)
    assert Solution().hasCycle(head) == False


def test_example_4():
    # head = [1, 2], pos = -1
    head = build_linked_list_with_cycle([1, 2], -1)
    assert Solution().hasCycle(head) == False
