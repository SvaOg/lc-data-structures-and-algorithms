"""
2294. Partition Array Such That Maximum Difference Is K

You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [3,6,1,2,5], k = 2
Output: 2
Explanation:
We can partition nums into the subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
Since two subsequences were created, we return 2.
It can be shown that 2 is the minimum number of subsequences needed.

Example 2:
Input: nums = [1,2,3], k = 1
Output: 2
Explanation:
We can partition nums into the subsequences [1,2] and [3].
The difference between the maximum and minimum value in the first subsequence is 2 - 1 = 1.
The difference between the maximum and minimum value in the second subsequence is 3 - 3 = 0.
Since two subsequences were created, we return 2.
It can be shown that 2 is the minimum number of subsequences needed.

Example 3:
Input: nums = [2,2,4,5], k = 0
Output: 3
Explanation:
We can partition nums into the subsequences [2], [2], and [4,5].
The difference between the maximum and minimum value in the first subsequences is 2 - 2 = 0.
The difference between the maximum and minimum value in the second subsequences is 2 - 2 = 0.
The difference between the maximum and minimum value in the third subsequences is 5 - 4 = 1.
Since three subsequences were created, we return 3.
It can be shown that 3 is the minimum number of subsequences needed.

Constraints:
- 1 <= nums.length <= 105
- 0 <= nums[i] <= 105
- 0 <= k <= 105
"""

from typing import List
import pytest


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        curr_min, count = None, None
        for v in sorted(nums):
            if curr_min is None:
                curr_min = v
                count = 1
            else:
                if curr_min + k < v:
                    curr_min = v
                    count += 1
        return count


@pytest.fixture
def sln():
    return Solution()


def test_example_1(sln):
    assert sln.partitionArray([3, 6, 1, 2, 5], 2) == 2


def test_example_2(sln):
    assert sln.partitionArray([1, 2, 3], 1) == 2


def test_example_3(sln):
    assert sln.partitionArray([2, 2, 4, 5], 0) == 3
