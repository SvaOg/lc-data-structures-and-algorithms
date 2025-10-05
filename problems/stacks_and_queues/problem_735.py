"""
LeetCode Problem 735: Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:
Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 move left, and 1 and 2 move right. Asteroids moving in the same direction never meet, so no asteroids will meet each other.

Constraints:
- 2 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0
"""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for n in asteroids:
            stack.append(n)

            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                n1, n2 = stack[-2:]
                stack.pop()
                stack.pop()

                if abs(n1) > abs(n2):
                    stack.append(n1)
                elif abs(n1) < abs(n2):
                    stack.append(n2)

        return stack


import pytest


def test_example_1():
    """
    Example 1:
    Input: asteroids = [5,10,-5]
    Output: [5,10]
    """
    sol = Solution()
    assert sol.asteroidCollision([5, 10, -5]) == [5, 10]


def test_example_2():
    """
    Example 2:
    Input: asteroids = [8,-8]
    Output: []
    """
    sol = Solution()
    assert sol.asteroidCollision([8, -8]) == []


def test_example_3():
    """
    Example 3:
    Input: asteroids = [10,2,-5]
    Output: [10]
    """
    sol = Solution()
    assert sol.asteroidCollision([10, 2, -5]) == [10]


def test_example_4():
    """
    Example 4:
    Input: asteroids = [-2,-1,1,2]
    Output: [-2,-1,1,2]
    """
    sol = Solution()
    assert sol.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
