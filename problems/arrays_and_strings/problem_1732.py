"""
1732. Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

Constraints:
- n == gain.length
- 1 <= n <= 100
- -100 <= gain[i] <= 100

Problem link: https://leetcode.com/problems/find-the-highest-altitude/
"""

from typing import List
import pytest


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_sum, max_sum = 0, 0
        for n in range(len(gain)):
            curr_sum += gain[n]
            max_sum = max(max_sum, curr_sum)
        return max_sum


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    gain = [-5, 1, 5, 0, -7]
    expected = 1
    assert sln.largestAltitude(gain) == expected


def test_example_2(sln):
    gain = [-4, -3, -2, -1, 4, 3, 2]
    expected = 0
    assert sln.largestAltitude(gain) == expected
