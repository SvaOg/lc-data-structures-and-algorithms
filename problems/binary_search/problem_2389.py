"""
2389. Longest Subsequence With Limited Sum

https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

You are given an integer array nums and an integer array queries. For each queries[i],
determine the maximum size of a subsequence that you can take from nums such that the sum
of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no
elements without changing the order of the remaining elements.

Return an array answer of length queries.length where answer[i] is the answer to the i-th query.

Example 1:
Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation:
- For queries[0] = 3, we can take subsequence [2,1] with sum 3 (length 2).
- For queries[1] = 10, we can take subsequence [4,5,1] with sum 10 (length 3).
- For queries[2] = 21, we can take all elements [4,5,2,1] with sum 12 (length 4).

Example 2:
Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The sum of any subsequence cannot be less than or equal to 1, so the answer is 0.

Constraints:
- 1 <= nums.length, queries.length <= 1000
- 1 <= nums[i], queries[i] <= 10^6
"""

from bisect import bisect_right
from typing import List
import pytest


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Create a copy of nums, so I don't change nums
        sums = nums[:]

        # Sort array, so I could use binary search later
        sums.sort()

        # Create a prefix sum array
        for n in range(1, len(sums)):
            sums[n] += sums[n - 1]

        return [bisect_right(sums, q) for q in queries]


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    assert sln.answerQueries(nums, queries) == [2, 3, 4]


def test_002(sln):
    """Test the second example from the problem description."""
    nums = [2, 3, 4, 5]
    queries = [1]
    assert sln.answerQueries(nums, queries) == [0]
