"""
1338. Reduce Array Size to The Half

Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of such a set so that at least half of the integers of the array are removed.

Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choose the set {3, 5}, of size 2. Removing all their occurrences from arr results in [2,2,7].
Now the size of arr is 3 and half of the original size is 5. So, we have removed at least half of the integers.
There is no set of size 1 that satisfies the condition.

Example 2:
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only set you can choose is {7}. This makes the size of arr 0 which is less than half of the original size.

Constraints:
- 2 <= arr.length <= 10^5
- arr.length is even.
- 1 <= arr[i] <= 10^5
"""

from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = [-f for f in Counter(arr).values()]
        heapify(freq)

        half_size = len(arr) / 2
        count, removed = 0, 0

        while removed < half_size and freq:
            count += 1
            removed -= heappop(freq)

        return count

    def minSetSize_sort(self, arr: List[int]) -> int:
        freq = sorted(Counter(arr).values(), reverse=True)
        half_size = len(arr) / 2

        count, removed = 0, 0
        for f in freq:
            count += 1
            removed += f
            if removed >= half_size:
                break

        return count


import pytest


def test_example1():
    arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    expected = 2
    assert Solution().minSetSize(arr) == expected


def test_example2():
    arr = [7, 7, 7, 7, 7, 7]
    expected = 1
    assert Solution().minSetSize(arr) == expected


def test_example2():
    arr = [7, 7, 7, 7, 7, 7]
    expected = 1
    assert Solution().minSetSize(arr) == expected
