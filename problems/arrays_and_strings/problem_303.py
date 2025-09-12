"""
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Constraints:
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls will be made to sumRange.

Problem link: https://leetcode.com/problems/range-sum-query-immutable/
"""

import pytest


class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [nums[0]]
        for n in range(1, len(nums)):
            self.prefix.append(self.prefix[-1] + nums[n])

    def sumRange(self, left: int, right: int) -> int:
        return (
            self.prefix[right] - self.prefix[left - 1] if left else self.prefix[right]
        )


def test_numArray_example1():
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    assert numArray.sumRange(0, 2) == 1
    assert numArray.sumRange(2, 5) == -1
    assert numArray.sumRange(0, 5) == -3
