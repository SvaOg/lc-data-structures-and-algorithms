"""
216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true: Only numbers 1 through 9 are used. Each number is used at most once. Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

Example 3:
Input: k = 4, n = 1
Output: []

Constraints:
2 <= k <= 9
1 <= n <= 60
"""

from typing import List
import pytest


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(i, curr, reminder):
            if len(curr) == k:
                if reminder == 0:
                    result.append(curr[:])
                return

            for j in range(i, 10):
                if reminder >= j:
                    curr.append(j)
                    backtrack(j + 1, curr, reminder - j)
                    curr.pop()

        result = []
        backtrack(1, [], n)
        return result


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    k = 3
    n = 7
    assert sln.combinationSum3(k, n) == [[1, 2, 4]]


def test_002(sln):
    """Test the second example from the problem description."""
    k = 3
    n = 9
    assert sorted(sln.combinationSum3(k, n)) == sorted(
        [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    )


def test_003(sln):
    """Test the third example from the problem description."""
    k = 4
    n = 1
    assert sln.combinationSum3(k, n) == []
