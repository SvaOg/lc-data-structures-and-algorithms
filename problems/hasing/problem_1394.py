"""
1394. Find Lucky Integer in an Array
https://leetcode.com/problems/find-lucky-integer-in-an-array/

Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency of 2 is 2.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

Constraints:
- 1 <= arr.length <= 500
- 1 <= arr[i] <= 500
"""

from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n = len(arr)

        freq = [0] * n

        for num in arr:
            if num - 1 < n:
                freq[num - 1] += 1

        max_freq = -1
        for i, f in enumerate(freq):
            if i + 1 == f:
                max_freq = max(max_freq, f)

        return max_freq

    def findLucky1(self, arr: List[int]) -> int:
        n = len(arr)

        for v in arr:
            num = v & 1023
            if num - 1 < n:
                arr[num - 1] += 1024

        max_freq = -1
        for i in range(n):
            num = i + 1
            freq = arr[i] >> 10
            if num == freq:
                max_freq = max(max_freq, freq)

        return max_freq

    def findLucky2(self, arr: List[int]) -> int:
        try:
            return max([num for num, freq in Counter(arr).items() if num == freq])
        except ValueError:
            return -1


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    arr = [2, 2, 3, 4]
    assert solution.findLucky(arr) == 2


def test_example_2(solution):
    arr = [1, 2, 2, 3, 3, 3]
    assert solution.findLucky(arr) == 3


def test_example_3(solution):
    arr = [2, 2, 2, 3, 3]
    assert solution.findLucky(arr) == -1
