"""
2540. Minimum Common Value

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 3:
Input: nums1 = [1,2,3], nums2 = [4,5,6]
Output: -1
Explanation: There is no common element, so we return -1.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[j] <= 10^9
- Both nums1 and nums2 are sorted in non-decreasing order.

Problem link: https://leetcode.com/problems/minimum-common-value/
"""

from typing import List
import pytest


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        return -1

    def getCommon1(self, nums1: List[int], nums2: List[int]) -> int:
        v = set(nums1) & set(nums2)
        return min(v) if v else -1


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    nums1 = [1, 2, 3]
    nums2 = [2, 4]
    expected = 2
    assert sln.getCommon(nums1, nums2) == expected


def test_example_2(sln):
    nums1 = [1, 2, 3, 6]
    nums2 = [2, 3, 4, 5]
    expected = 2
    assert sln.getCommon(nums1, nums2) == expected


def test_example_3(sln):
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    expected = -1
    assert sln.getCommon(nums1, nums2) == expected
