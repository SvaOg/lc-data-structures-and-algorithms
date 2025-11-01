"""
1231. Divide Chocolate

Editorial (awesome): https://leetcode.com/problems/divide-chocolate/editorial/

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array `sweetness`.
You want to share the chocolate with your `k` friends so you start cutting the chocolate bar into `k + 1` pieces, each piece consists of a contiguous subarray of `sweetness`.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Example 1:
Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to be [1,2,3], [4,5], [6], [7], [8], [9]. The minimum sweetness piece has total sweetness 6 and that is what you will eat.

Example 2:
Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There are 9 people including you. No matter how you cut, the smallest piece you can guarantee is 1.

Example 3:
Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to be [1,2,2], [1,2,2], [1,2,2]. The minimum piece has total sweetness 5.

Constraints:
- 1 <= sweetness.length <= 10^5
- 0 <= k < sweetness.length
- 1 <= sweetness[i] <= 10^9
"""

from math import ceil
from typing import List
import pytest


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        number_of_people = k + 1
        left = min(sweetness)
        right = sum(sweetness) // number_of_people

        while left < right:
            mid = (left + right + 1) // 2

            curr_sweetness = 0
            people_with_chocolate = 0
            for s in sweetness:
                curr_sweetness += s
                if curr_sweetness >= mid:
                    people_with_chocolate += 1
                    curr_sweetness = 0

            if people_with_chocolate >= number_of_people:
                left = mid
            else:
                right = mid - 1

        return left


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 5
    assert sln.maximizeSweetness(sweetness, k) == 6


def test_002(sln):
    """Test the second example from the problem description."""
    sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    k = 8
    assert sln.maximizeSweetness(sweetness, k) == 1


def test_003(sln):
    """Test the third example from the problem description."""
    sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2]
    k = 2
    assert sln.maximizeSweetness(sweetness, k) == 5
