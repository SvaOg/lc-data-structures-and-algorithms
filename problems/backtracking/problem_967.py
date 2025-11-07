"""
967. Numbers With Same Consecutive Differences
https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/

You are given two integers n and k. Return a list of all non-negative integers of length n such that the absolute difference between every pair of consecutive digits is k. Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid; however, 0 is a valid number if n == 1. You may return the answer in any order.

Example 1:
Input: n = 3, k = 7
Output: [181, 292, 707, 818, 929]
Explanation: The only possible numbers are 181, 292, 707, 818, and 929. Note that 070 is not a valid number because it has a leading zero.

Example 2:
Input: n = 2, k = 1
Output: [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]

Example 3:
Input: n = 2, k = 0
Output: [11, 22, 33, 44, 55, 66, 77, 88, 99]

Constraints:
1 <= n <= 9
0 <= k <= 9
"""

from collections import defaultdict
from typing import List
import pytest


class Solution:
    """
    Tricky parts are edge cases (0 could not be first digit, k == 0)
    """

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr):
            if len(curr) == n:
                factor = 1
                num = 0
                for v in reversed(curr):
                    num += factor * v
                    factor *= 10
                result.append(num)
                return

            if curr:
                last_digit = int(curr[-1])
                candidates = (last_digit - k, last_digit + k) if k else (last_digit,)
                for next_digit in candidates:
                    if 0 <= next_digit <= 9:
                        curr.append(next_digit)
                        backtrack(curr)
                        curr.pop()
            else:
                for i in range(1, 10):
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()

        result = []
        backtrack([])
        return result


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    n = 3
    k = 7
    assert sorted(sln.numsSameConsecDiff(n, k)) == sorted([181, 292, 707, 818, 929])


def test_002(sln):
    """Test the second example from the problem description."""
    n = 2
    k = 1
    assert sln.numsSameConsecDiff(n, k) == [
        10,
        12,
        21,
        23,
        32,
        34,
        43,
        45,
        54,
        56,
        65,
        67,
        76,
        78,
        87,
        89,
        98,
    ]


def test_003(sln):
    """Test the third example from the problem description."""
    n = 2
    k = 0
    assert sln.numsSameConsecDiff(n, k) == [
        11,
        22,
        33,
        44,
        55,
        66,
        77,
        88,
        99,
    ]
