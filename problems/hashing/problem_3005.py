"""
3005. Count Elements With Maximum Frequency
https://leetcode.com/problems/count-elements-with-maximum-frequency/

You are given an array nums consisting of positive integers.

Return the total number of elements in nums such that the frequency of that element is equal to the maximum frequency.

Example 1:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array. So the answer is 2 + 2 = 4.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements have a frequency of 1 which is the maximum.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = 0
        count = 0
        for freq in Counter(nums).values():
            if freq > max_freq:
                max_freq = freq
                count = 1
            elif freq == max_freq:
                count += 1
        return max_freq * count
    
    def maxFrequencyElements2(self, nums: List[int]) -> int:
        sum = 0

        freq = sorted(Counter(nums).values(), reverse=True)
        f1 = freq[0]

        for n in freq:
            if n != f1:
                break
            sum += n

        return sum


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    nums = [1, 2, 2, 3, 1, 4]
    assert solution.maxFrequencyElements(nums) == 4


def test_example_2(solution):
    nums = [1, 2, 3, 4, 5]
    assert solution.maxFrequencyElements(nums) == 5
