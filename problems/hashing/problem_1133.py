"""
LeetCode Problem 1133: Largest Unique Number

Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

Example 1:

Input: A = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation:
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so the answer is 8.

Example 2:

Input: A = [9,9,8,8]
Output: -1
Explanation:
There is no number that occurs only once.

Constraints:
- 1 <= A.length <= 2000
- 1 <= A[i] <= 1000
"""

from collections import Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        once = set()
        other = set()
        for v in nums:
            if v in other:
                continue
            elif v in once:
                once.remove(v)
                other.add(v)
            else:
                once.add(v)
        return sorted(once)[-1] if once else -1


def test_largestUniqueNumber():
    solution = Solution()

    # Test case 1
    A1 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    expected1 = 8
    assert solution.largestUniqueNumber(A1) == expected1

    # Test case 2
    A2 = [9, 9, 8, 8]
    expected2 = -1
    assert solution.largestUniqueNumber(A2) == expected2
