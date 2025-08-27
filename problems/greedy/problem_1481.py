"""
1481. Least Number of Unique Integers after K Removals

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, remove 2 and remove 1 twice. 3 is left.

Example 3:
Input: arr = [2,4,1,8,3,5,1,3], k = 3
Output: 3

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^9
- 0 <= k <= arr.length
"""

from typing import List
import pytest
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = sorted(Counter(arr).values())

        n = 0
        while n < len(freq) and k >= freq[n]:
            k -= freq[n]
            n += 1

        return len(freq) - n


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    assert sln.findLeastNumOfUniqueInts([5, 5, 4], 1) == 1


def test_example_2(sln):
    assert sln.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3) == 2


def test_example_3(sln):
    assert sln.findLeastNumOfUniqueInts([2, 4, 1, 8, 3, 5, 1, 3], 3) == 3
