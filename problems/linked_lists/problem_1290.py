"""
1290. Convert Binary Number in a Linked List to Integer
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Constraints:
- The Linked List is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.
"""

from typing import Optional
from .linked_lists import (
    ListNode,
    build_linked_list,
    linked_list_to_list,
)
import pytest


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = head
        number = 0
        while curr:
            number = (number << 1) + curr.val
            curr = curr.next
        return number


def test_example_1():
    head = build_linked_list([1, 0, 1])
    expected = 5
    result = Solution().getDecimalValue(head)
    assert result == expected


def test_example_2():
    head = build_linked_list([0])
    expected = 0
    result = Solution().getDecimalValue(head)
    assert result == expected
