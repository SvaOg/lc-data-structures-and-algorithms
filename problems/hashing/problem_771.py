"""
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

Constraints:
- 1 <= jewels.length, stones.length <= 50
- jewels and stones consist of only English letters.
- All the characters of jewels are unique.
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        good_stones = [ch for ch in stones if ch in jewels]
        return len(good_stones)


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.numJewelsInStones("aA", "aAAbbbb") == 3


def test_example_2(solution):
    assert solution.numJewelsInStones("z", "ZZ") == 0
