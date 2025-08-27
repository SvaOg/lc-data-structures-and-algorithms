"""2260. Minimum Consecutive Cards to Pick Up
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

Given an integer array cards, find the minimum number of consecutive cards you need to pick up to have a pair of matching cards. If it is impossible to have matching cards, return -1.

Example 1:
Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

Example 2:
Input: cards = [1,0,5,3]
Output: -1
Explanation: No two cards have the same value, so it is impossible to have matching cards.

Constraints:
1 <= cards.length <= 10^5
0 <= cards[i] <= 10^6
"""

from turtle import position
from typing import List
from collections import defaultdict
import pytest


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float("inf")
        positions = {}
        for i, card in enumerate(cards):
            pos = positions.get(card, -1)
            if pos >= 0:
                ans = min(ans, i - pos + 1)
            positions[card] = i
        return ans if ans < float("inf") else -1

@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.minimumCardPickup([3, 4, 2, 3, 4, 7]) == 4


def test_example_2(solution):
    assert solution.minimumCardPickup([1, 0, 5, 3]) == -1


def test_single_card(solution):
    assert solution.minimumCardPickup([1]) == -1


def test_all_same(solution):
    assert solution.minimumCardPickup([2, 2, 2]) == 2


def test_pair_at_ends(solution):
    assert solution.minimumCardPickup([5, 1, 2, 3, 4, 5]) == 6


def test_wrong_answer_001(solution):
    assert (
        solution.minimumCardPickup(
            [
                95,
                11,
                8,
                65,
                5,
                86,
                30,
                27,
                30,
                73,
                15,
                91,
                30,
                7,
                37,
                26,
                55,
                76,
                60,
                43,
                36,
                85,
                47,
                96,
                6,
            ]
        )
        == 3
    )
