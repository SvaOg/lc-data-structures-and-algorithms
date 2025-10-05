"""
LeetCode Problem 946: Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Constraints:
- 1 <= pushed.length <= 1000
- 0 <= pushed[i] <= 1000
- All the elements of pushed are unique.
- popped.length == pushed.length
- popped is a permutation of pushed.
"""


class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []

        def try_pop(curr_pos):
            if stack and stack[-1] == popped[curr_pos]:
                stack.pop()
                return True
            return False

        curr_pos = 0
        for n in pushed:
            stack.append(n)
            while try_pop(curr_pos):
                curr_pos += 1

        return not stack


import pytest


def test_example_1():
    """
    Example 1:
    Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: true
    """
    sol = Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    assert sol.validateStackSequences(pushed, popped) == True


def test_example_2():
    """
    Example 2:
    Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    Output: false
    """
    sol = Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    assert sol.validateStackSequences(pushed, popped) == False
