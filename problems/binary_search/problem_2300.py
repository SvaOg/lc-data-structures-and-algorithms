"""
2300. Successful Pairs of Spells and Potions

Given two positive integer arrays spells and potions of lengths n and m respectively,
where spells[i] represents the strength of the i-th spell and potions[j] represents the
strength of the j-th potion.

You are also given an integer success. A spell and potion pair is considered successful if
their product is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will
form a successful pair with the i-th spell.

Example 1:
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- For the 0-th spell (5), the products with potions are [5,10,15,20,25]. Four of them are
  at least 7: potions [2,3,4,5].
- For the 1-st spell (1), the products are [1,2,3,4,5]. None are at least 7.
- For the 2-nd spell (3), the products are [3,6,9,12,15]. Three are at least 7: potions [3,4,5].

Example 2:
Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- For the 0-th spell (3), products are [24,15,24]. Two are at least 16.
- For the 1-st spell (1), products are [8,5,8]. None are at least 16.
- For the 2-nd spell (2), products are [16,10,16]. Two are at least 16.

Constraints:
- n == spells.length
- m == potions.length
- 1 <= n, m <= 10^5
- 1 <= spells[i], potions[j] <= 10^5
- 1 <= success <= 10^10
"""

from typing import List
import pytest
from bisect import bisect_left
from math import ceil


class Solution:
    """
    Approach is to sort the potions and do binary search on them to look for insertion point, because if
    potion is strong enough to succeed, the stronger potions will succeed as well.
    """

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        # def bisect_left(arr, target):
        #     left = 0
        #     right = len(arr)
        #     while left < right:
        #         mid = (left + right) // 2
        #         if arr[mid] >= target:
        #             right = mid
        #         else:
        #             left = mid + 1
        #     return left

        n = len(potions)
        potions.sort()

        ans = []
        for strength in spells:
            target = ceil(success / strength)
            pos = bisect_left(potions, target)
            ans.append(n - pos)
        return ans


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    assert sln.successfulPairs(spells, potions, success) == [4, 0, 3]


def test_002(sln):
    """Test the second example from the problem description."""
    spells = [3, 1, 2]
    potions = [8, 5, 8]
    success = 16
    assert sln.successfulPairs(spells, potions, success) == [2, 0, 2]
