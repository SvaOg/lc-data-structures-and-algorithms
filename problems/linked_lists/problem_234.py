"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional
from src.my_leetcode.linked_lists import (
    ListNode,
    build_linked_list,
    linked_list_to_list,
)
import pytest


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def backtrack(right):
            nonlocal left, stop, is_palindrome

            # Base case
            if not right:
                return

            # Recurse
            backtrack(right.next)

            if stop:
                return

            # Nodes crossed over, stop processing
            if right == left or right.next == left:
                stop = True
                return

            if left.val != right.val:
                is_palindrome = False
                stop = True
                return

            left = left.next

        if not head.next:
            return True

        left = head
        is_palindrome, stop = True, False

        backtrack(head)

        return is_palindrome


def test_example_1():
    head = build_linked_list([1, 2, 2, 1])
    expected = True
    result = Solution().isPalindrome(head)
    assert result == expected


def test_example_2():
    head = build_linked_list([1, 2])
    expected = False
    result = Solution().isPalindrome(head)
    assert result == expected
