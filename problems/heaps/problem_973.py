"""
LeetCode Problem 973: K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance
(i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation:
The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
- 1 <= k <= points.length <= 10^4
- -10^4 < xi, yi < 10^4
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Use Top K approach:
    https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/708/heaps/4641/
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # We'll need max heap here to discard worst (farthers) elemnts
        for x, y in points:
            dist_squared = x * x + y * y
            heappush(heap, (-dist_squared, [x, y]))
            if len(heap) > k:
                heappop(heap)

        return [point for dist, point in heap]


import pytest


def test_example1():
    points = [[1, 3], [-2, 2]]
    k = 1
    expected = [[-2, 2]]
    result = Solution().kClosest(points, k)
    # Checking if result contains the expected points and has correct size
    assert sorted(map(sorted, result)) == sorted(map(sorted, expected))


def test_example2():
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    expected1 = [[3, 3], [-2, 4]]
    expected2 = [[-2, 4], [3, 3]]
    result = Solution().kClosest(points, k)
    # Since answer may be in any order, compare as sets
    assert sorted(map(sorted, result)) == sorted(map(sorted, expected1)) or sorted(
        map(sorted, result)
    ) == sorted(map(sorted, expected2))
