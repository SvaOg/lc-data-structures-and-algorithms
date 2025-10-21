"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
- 1 <= k <= arr.length
- 1 <= arr.length <= 10^4
- arr is sorted in ascending order.
- -10^4 <= arr[i], x <= 10^4
"""

from heapq import heappop, heappush, heapreplace
from typing import List
import pytest


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap = []

        for n in arr:
            heappush(maxheap, (-abs(n - x), -n))
            if len(maxheap) > k:
                heappop(maxheap)

        return sorted(-n for _, n in maxheap)


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    expected = [1, 2, 3, 4]
    assert solution.findClosestElements(arr, k, x) == expected


def test_example_2(solution):
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = -1
    expected = [1, 2, 3, 4]
    assert solution.findClosestElements(arr, k, x) == expected
