"""2342. Max Sum of a Pair With Equal Sum of Digits
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2): The sum of digits of nums[0] and nums[2] are equal: 1 + 8 = 3 + 6
- (1, 4): The sum of digits of nums[1] and nums[4] are equal: 4 + 3 = 7
Therefore, the maximum sum that we can obtain is nums[1] + nums[4] = 43 + 7 = 50.

Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.

Constraints:
* 2 <= nums.length <= 10^5
* 1 <= nums[i] <= 10^9
"""

from collections import defaultdict
from typing import List
import pytest


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            return sum

        ans = -1

        dic = {}
        for n in nums:
            key = get_digit_sum(n)
            curr = dic.get(key, -1)
            if curr >= 0:
                ans = max(ans, n + curr)
            dic[key] = max(n, curr)

        return ans


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.maximumSum([18, 43, 36, 13, 7]) == 54


def test_example_2(solution):
    assert solution.maximumSum([10, 12, 19, 14]) == -1


def test_empty_array(solution):
    assert solution.maximumSum([]) == -1


def test_single_element(solution):
    assert solution.maximumSum([42]) == -1


def test_all_same_digit_sums(solution):
    assert solution.maximumSum([11, 11, 11]) == 22