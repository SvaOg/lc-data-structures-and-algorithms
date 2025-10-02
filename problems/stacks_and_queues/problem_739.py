"""
LeetCode Problem 739: Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Explanation:
    - For day 0: 73 -> next warmer is 74 at day 1 (1 day)
    - For day 1: 74 -> next warmer is 75 at day 2 (1 day)
    - For day 2: 75 -> next warmer is 76 at day 6 (4 days)
    - For day 3: 71 -> next warmer is 72 at day 5 (2 days)
    - For day 4: 69 -> next warmer is 72 at day 5 (1 day)
    - For day 5: 72 -> next warmer is 76 at day 6 (1 day)
    - For day 6: 76 -> no warmer day (0)
    - For day 7: 73 -> no warmer day (0)

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Explanation: Each day is warmer than the previous one.

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""

from typing import List
import pytest


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        stack = []
        for pos, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                i = stack.pop()
                answer[i] = pos - i
            stack.append(pos)

        return answer


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Example 1: General case with multiple waits"""
    input = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]

    assert sln.dailyTemperatures(input) == expected


def test_002(sln):
    """Example 2: Strictly increasing temperatures"""
    assert sln.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]


def test_003(sln):
    """Example 3: Only one wait per day, last day has no warmer day"""
    assert sln.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
