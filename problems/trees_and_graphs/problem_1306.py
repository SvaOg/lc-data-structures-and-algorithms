"""
1306. Jump Game III

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], provided you are within the bounds of the array. You must not visit the same index more than once.

Return true if you can reach any index with value 0, or false otherwise.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3

Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3

Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation:
There is no way to reach at index 1 with value 0.
"""

from collections import deque


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)

        queue = deque([start])
        seen = set([start])

        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True

            for neighbor in (node + arr[node], node - arr[node]):
                if 0 <= neighbor < n and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return False


import pytest


@pytest.mark.parametrize(
    "arr,start,expected",
    [
        ([4, 2, 3, 0, 3, 1, 2], 5, True),  # Example 1
    ],
)
def test_example1(arr, start, expected):
    assert Solution().canReach(arr, start) == expected


@pytest.mark.parametrize(
    "arr,start,expected",
    [
        ([4, 2, 3, 0, 3, 1, 2], 0, True),  # Example 2
    ],
)
def test_example2(arr, start, expected):
    assert Solution().canReach(arr, start) == expected


@pytest.mark.parametrize(
    "arr,start,expected",
    [
        ([3, 0, 2, 1, 2], 2, False),  # Example 3
    ],
)
def test_example3(arr, start, expected):
    assert Solution().canReach(arr, start) == expected
