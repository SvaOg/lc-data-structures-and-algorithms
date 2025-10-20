"""
1962. Remove Stones to Minimize the Total
https://leetcode.com/problems/remove-stones-to-minimize-the-total/

You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

- Choose any pile of stones and remove floor(piles[i] / 2) stones from it.

Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

Example 1:
Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones left is 3 + 4 + 5 = 12.

Example 2:
Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,3,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones left is 2 + 3 + 3 + 4 = 12.

Constraints:
- 1 <= piles.length <= 10^5
- 1 <= piles[i] <= 10^4
- 1 <= k <= 10^5
"""

from typing import List
from heapq import heapify, heappop, heappush
import pytest


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # We need to use max heap, for that we need to negate numbers in piles
        piles = [-n for n in piles]

        heapify(piles)

        for _ in range(k):
            # Remove largest pile, half its size, and put it back
            largest_pile = -heappop(piles)
            new_pile = largest_pile - (largest_pile // 2)
            heappush(piles, -new_pile)
        
        return -sum(piles)


@pytest.mark.parametrize(
    "piles,k,expected",
    [
        ([5, 4, 9], 2, 12),
    ],
)
def test_example_1(piles, k, expected):
    assert Solution().minStoneSum(piles, k) == expected


@pytest.mark.parametrize(
    "piles,k,expected",
    [
        ([4, 3, 6, 7], 3, 12),
    ],
)
def test_example_2(piles, k, expected):
    assert Solution().minStoneSum(piles, k) == expected
