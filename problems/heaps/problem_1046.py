"""
1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

* If x == y, both stones are destroyed
* If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:
* 1 <= stones.length <= 30
* 1 <= stones[i] <= 1000
"""

import heapq
from typing import List
import pytest


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        On each smash, at least one rock is destroyed, so there can be at most n iterations.
        At each iteration, we perform pops and pushes on the heap, which has a length of n at the start.
        This gives us a time complexity of O(n*log n). The heap uses O(n) space.
        """
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, -abs(stone1 - stone2))

        return -stones[0] if stones else 0


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1


def test_example_2(solution):
    assert solution.lastStoneWeight([1]) == 1


def test_empty_array(solution):
    assert solution.lastStoneWeight([]) == 0


def test_all_same(solution):
    assert solution.lastStoneWeight([2, 2, 2]) == 2


def test_two_stones(solution):
    assert solution.lastStoneWeight([5, 3]) == 2
