"""
1870. Minimum Speed to Arrive on Time

You are given an integer array dist of length n, where dist[i] is the distance (in kilometers) of the i-th train ride. You are also given a floating-point number hour, representing the total amount of time you have to arrive at the office.

You will commute by train n times. The i-th train ride takes exactly dist[i] / speed hours at an integer speed speed (in km/h). However, trains depart at integer hours, so except for the last ride, you must wait for the next integer hour to depart. Therefore, the time taken to complete the i-th ride is ceil(dist[i] / speed) hours for each i from 0 to n - 2, and dist[n - 1] / speed hours for the last ride.

Return the minimum positive integer speed (in km/h) that allows you to arrive on or before hour. If it is impossible to arrive on time, return -1.

Example 1:
Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed = 1, total time = ceil(1/1) + ceil(3/1) + 2/1 = 1 + 3 + 2 = 6.

Example 2:
Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed = 3, total time = ceil(1/3) + ceil(3/3) + 2/3 = 1 + 1 + 0.6667 = 2.6667 <= 2.7. Any lower integer speed does not work.

Example 3:
Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: Regardless of speed, the first two rides each take at least 1 hour due to waiting, so total time is at least 2 hours.

Constraints:
- 1 <= n == dist.length <= 10^5
- 1 <= dist[i] <= 10^5
- 1 <= hour <= 10^9 (hour is a floating-point number and may have up to two decimal places)
"""

from math import ceil
from typing import List
import pytest


class Solution:
    """
    Binary search through solution space. Need to be careful around edge cases.
    (Last train do not add an extra hour, for example)
    """

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1

        def check(k):
            t = 0
            for d in dist:
                t = ceil(t) + d / k
            return t <= hour

        left = 1
        # right = 10**7
        right = max(dist) + 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    dist = [1, 3, 2]
    hour = 6
    assert sln.minSpeedOnTime(dist, hour) == 1


def test_002(sln):
    """Test the second example from the problem description."""
    dist = [1, 3, 2]
    hour = 2.7
    assert sln.minSpeedOnTime(dist, hour) == 3


def test_003(sln):
    """Test the third example from the problem description."""
    dist = [1, 3, 2]
    hour = 1.9
    assert sln.minSpeedOnTime(dist, hour) == -1
