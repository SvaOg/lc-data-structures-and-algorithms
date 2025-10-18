"""
909. Snakes and Ladders

You are given an n x n integer matrix board where the cells are labeled from 1 to n^2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

- Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n^2)].
    - This choice simulates the result of a standard 6-sided die roll: i.e., there are always up to 6 options for the destination square (even if moving would go past the end of the board).
- If next is not a snake or a ladder (that is, board[x][y] == -1), you must move to square next.
- If next is a ladder or snake (i.e. board[x][y] != -1), you must move to the destination of that ladder or snake, board[x][y].
Note that you only take a snake or ladder at the end of a move so, if you encounter a snake or ladder on the way, you do not immediately move to its destination unless you have reached the end of your die roll.
Return the least number of moves required to reach square n^2. If it is not possible to reach square n^2, return -1.

Example 1:
Input: board = [
  [-1,-1,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1,-1],
  [-1,35,-1,-1,13,-1],
  [-1,-1,-1,-1,-1,-1],
  [-1,15,-1,-1,-1,-1]
]
Output: 4
Explanation:
In the beginning, you start at square 1 [at the bottom-left corner].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
A total of 4 moves are required to reach the last square.

Example 2:
Input: board = [[-1,-1],[-1,3]]
Output: 1

Constraints:
- n == board.length == board[i].length
- 2 <= n <= 20
- board[i][j] is either -1 or in the range [1, n^2].
- The board square with a snake or ladder always has a destination that is different from itself.
- The board square with a snake or ladder does not connect to another snake or ladder.
"""

from collections import deque
from typing import List
import pytest


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        last_cell = n * n

        linear = [0]

        even = True
        for i in range(n - 1, -1, -1):
            linear.extend(board[i] if even else board[i][::-1])
            even = not even

        queue = deque([(1, 1)])
        seen = {1}

        while queue:
            curr, steps = queue.popleft()
            for dice in range(1, 7):
                next = curr + dice
                if next == last_cell:
                    return steps

                if next in seen or n > last_cell:
                    continue

                seen.add(next)

                if linear[next] != -1:
                    next = linear[next]
                    if next == last_cell:
                        return steps

                queue.append((next, steps + 1))

        return -1


# Pytest test cases


def test_example1():
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    assert Solution().snakesAndLadders(board) == 4


def test_example2():
    board = [[-1, -1], [-1, 3]]
    assert Solution().snakesAndLadders(board) == 1


def test_example3():
    board = [[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]
    assert Solution().snakesAndLadders(board) == 1
