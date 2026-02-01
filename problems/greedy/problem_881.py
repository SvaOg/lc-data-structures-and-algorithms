"""
881. Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4

Constraints:
- 1 <= people.length <= 5 * 10^4
- 1 <= people[i] <= limit <= 3 * 10^4
"""

from typing import List
import pytest


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)

        left, right = 0, len(people) - 1
        boats = 0
        while True:
            boats += 1
            if left < right and people[left] + people[right] <= limit:
                right -= 1
            if left == right:
                break
            left += 1

        return boats


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    assert sln.numRescueBoats([1, 2], 3) == 1


def test_example_2(sln):
    assert sln.numRescueBoats([3, 2, 2, 1], 3) == 3


def test_example_3(sln):
    assert sln.numRescueBoats([3, 5, 3, 4], 5) == 4
