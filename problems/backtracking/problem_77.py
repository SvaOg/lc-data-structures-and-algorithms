"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
1 <= n <= 20
1 <= k <= n
"""

from typing import List
import pytest


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, idx):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for i in range(idx, n + 1):
                curr.append(i)
                backtrack(curr, i + 1)
                curr.pop()

        ans = []
        backtrack([], 1)
        return ans


@pytest.fixture
def sln():
    yield Solution()


def test_example_1(sln):
    """Test example 1 from the problem description."""
    n = 4
    k = 2
    expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert sln.combine(n, k) == expected


def test_example_2(sln):
    """Test example 2 from the problem description."""
    n = 1
    k = 1
    expected = [[1]]
    assert sln.combine(n, k) == expected
