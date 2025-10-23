"""
1833. Maximum Ice Cream Bars

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

You are given an array costs of positive integers, where costs[i] is the cost of the i-th ice cream bar. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible.

Note: The boy can buy the ice cream bars in any order and can buy each ice cream bar at most once.

Return the maximum number of ice cream bars the boy can buy with coins coins.

Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy the bars with costs 1, 1, 2, and 3 for a total of 7 coins.

Example 2:
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.

Example 3:
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars.

Constraints:
- 1 <= costs.length <= 10^5
- 1 <= costs[i] <= 10^5
- 1 <= coins <= 10^8
"""

from heapq import heapify, heappop
from typing import List
import pytest


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = costs[:]
        heapify(costs)

        ice_bars = 0
        while costs and coins >= costs[0]:
            coins -= heappop(costs)
            ice_bars += 1
        return ice_bars


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    costs = [1, 3, 2, 4, 1]
    coins = 7
    expected = 4
    assert sln.maxIceCream(costs, coins) == expected


def test_002(sln):
    """Test the second example from the problem description."""
    costs = [10, 6, 8, 7, 7, 8]
    coins = 5
    expected = 0
    assert sln.maxIceCream(costs, coins) == expected


def test_003(sln):
    """Test the third example from the problem description."""
    costs = [1, 6, 3, 1, 2, 5]
    coins = 20
    expected = 6
    assert sln.maxIceCream(costs, coins) == expected
