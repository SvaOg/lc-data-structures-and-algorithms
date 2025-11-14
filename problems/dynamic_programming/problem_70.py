"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2

Example 2:
Input: n = 3
Output: 3

Constraints:
1 <= n <= 45
"""

from typing import List
import pytest

"""
Similar to Fib(n) but the base case is different
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        arr = [0] * n
        arr[0] = 1
        arr[1] = 2

        for i in range(2, n):
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[-1]

    def climbStairs_top_down(self, n: int) -> int:
        def dp(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i not in memo:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        memo = {}
        return dp(n)


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    n = 2
    assert sln.climbStairs(n) == 2


def test_002(sln):
    """Test the second example from the problem description."""
    n = 3
    assert sln.climbStairs(n) == 3
