"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
"""

from typing import List
import pytest


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pass

@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    piles = [3,6,7,11]
    h = 8
    assert sln.minEatingSpeed(piles, h) == 4

def test_002(sln):
    """Test the second example from the problem description."""
    piles = [30,11,23,4,20]
    h = 5
    assert sln.minEatingSpeed(piles, h) == 30

def test_003(sln):
    """Test the third example from the problem description."""
    piles = [30,11,23,4,20]
    h = 6
    assert sln.minEatingSpeed(piles, h) == 23