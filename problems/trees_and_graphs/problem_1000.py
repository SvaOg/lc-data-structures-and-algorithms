"""
1000. Minimum Cost to Merge Stones

There are n piles of stones arranged in a row. The i-th pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

Example 1:
Input: stones = [3,2,4,1], k = 2
Output: 20
Explanation: We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.

Example 2:
Input: stones = [3,2,4,1], k = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore. So the task is impossible.

Example 3:
Input: stones = [3,5,1,2,6], k = 3
Output: 25
Explanation: We start with [3, 5, 1, 2, 6].
We merge [3, 5, 1] for a cost of 9, and we are left with [9, 2, 6].
We merge [2, 6] for a cost of 8, and we are left with [9, 8].
We merge [9, 8] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.

Constraints:
n == stones.length
1 <= n <= 30
1 <= stones[i] <= 100
2 <= k <= 30

Follow up: Can you solve this problem in O(n³) time complexity?
"""

from typing import List
import pytest


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        pass


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    stones = [3, 2, 4, 1]
    k = 2
    assert sln.mergeStones(stones, k) == 20


def test_002(sln):
    """Test the second example from the problem description."""
    stones = [3, 2, 4, 1]
    k = 3
    assert sln.mergeStones(stones, k) == -1


def test_003(sln):
    """Test the third example from the problem description."""
    stones = [3, 5, 1, 2, 6]
    k = 3
    assert sln.mergeStones(stones, k) == 25


def test_single_pile(sln):
    """Test with a single pile of stones."""
    stones = [5]
    k = 2
    assert sln.mergeStones(stones, k) == -1


def test_two_piles_k_equals_two(sln):
    """Test with two piles and k=2."""
    stones = [2, 3]
    k = 2
    assert sln.mergeStones(stones, k) == 5


def test_impossible_merge(sln):
    """Test case where merging is impossible."""
    stones = [1, 2, 3, 4]
    k = 4
    assert sln.mergeStones(stones, k) == 10
