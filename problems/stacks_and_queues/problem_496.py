"""
LeetCode Problem 496: Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
    - For nums1[0]=4, there is no next greater element in nums2, so output is -1.
    - For nums1[1]=1, the next greater element in nums2 is 3.
    - For nums1[2]=2, there is no next greater element in nums2, so output is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation:
    - For nums1[0]=2, the next greater element in nums2 is 3.
    - For nums1[1]=4, there is no next greater element in nums2, so output is -1.

Constraints:
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are unique.
- All the integers of nums1 also appear in nums2.

Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""

from typing import List
import pytest


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []

        for val in nums2:
            while stack and stack[-1] < val:
                hashmap[stack.pop()] = val
            stack.append(val)

        return [hashmap.get(v, -1) for v in nums1]

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        positions = {}
        next_greater = {}

        decreasing = []
        for pos, val in enumerate(nums2):
            # Creating a map to go from nums1 to nums2
            positions[val] = pos

            # Looking for next greater element for items to the left of pos
            while decreasing and nums2[decreasing[-1]] < val:
                next_greater[decreasing[-1]] = val
                decreasing.pop()

            decreasing.append(pos)

        ans = []
        for val in nums1:
            pos = positions[val]
            ans.append(next_greater.get(pos, -1))

        return ans


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """
    Example 1: General case with no next greater for some elements
    """
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    expected = [-1, 3, -1]
    assert sln.nextGreaterElement(nums1, nums2) == expected


def test_002(sln):
    """
    Example 2: Next greater exists for one element, not for the other
    """
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    expected = [3, -1]
    assert sln.nextGreaterElement(nums1, nums2) == expected
