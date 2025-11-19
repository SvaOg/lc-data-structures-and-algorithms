"""
322. Coin Change
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""

from typing import List
import pytest


class Solution:
    """
    Intuition: Iterative improvement. Solve the problem for only one coin,
    and then with each next coin see if you can improve the solution
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        # Use MAX_VAL = amount + 1 as "infinity"
        MAX_VAL = amount + 1

        # Initialize dp array
        dp = [MAX_VAL] * (amount + 1)

        # Base case
        dp[0] = 0

        for coin in coins:
            # Boundary check
            if coin > amount:
                continue
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != MAX_VAL else -1


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    coins = [1, 2, 5]
    amount = 11
    assert sln.coinChange(coins, amount) == 3


def test_002(sln):
    """Test the second example from the problem description."""
    coins = [2]
    amount = 3
    assert sln.coinChange(coins, amount) == -1


def test_003(sln):
    """Test the third example from the problem description."""
    coins = [1]
    amount = 0
    assert sln.coinChange(coins, amount) == 0
