"""347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
* k is in the range [1, the number of unique elements in the array]
* It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List
import pytest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for v in nums:
            freq[v] += 1

        heap = []
        for e, f in freq.items():
            heappush(heap, (f, e))
            if len(heap) > k:
                heappop(heap)

        return [e for f, e in heap]


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert sorted(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]


def test_example_2(solution):
    assert solution.topKFrequent([1], 1) == [1]


def test_all_same(solution):
    assert solution.topKFrequent([1, 1, 1, 1], 1) == [1]


def test_multiple_frequencies(solution):
    assert sorted(solution.topKFrequent([1, 1, 2, 2, 3, 3, 3], 2)) == [2, 3]
