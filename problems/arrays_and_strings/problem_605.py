"""
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some
are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return true if n new flowers can be
planted in the flowerbed without violating the no-adjacent-flowers rule and
false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length
"""

import pytest


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0
        length = len(flowerbed)

        while i < length and n > 0:
            if flowerbed[i] == 1:
                # Can't plant here or in the next spot
                i += 2
            elif i == length - 1 or flowerbed[i + 1] == 0:
                # We are at empty spot. If this is the last spot or the next is empty, plant here
                n -= 1
                i += 2
            else:
                # next spot is occupied, so we need to jump past it + 1
                i += 3

        return n <= 0


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """One flower can be placed in [1,0,0,0,1]."""
    assert sln.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True


def test_002(sln):
    """Two flowers cannot be placed in [1,0,0,0,1]."""
    assert sln.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False


def test_003(sln):
    """One flower cannot be placed in [0,0,1,0,0]."""
    assert sln.canPlaceFlowers([0, 0, 1, 0, 0], 1) is True
