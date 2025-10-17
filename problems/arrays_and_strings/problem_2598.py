"""
2598. Smallest Missing Non-negative Integer After Operations

You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

- For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to get nums = [-1,2,3].

The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

- For example, the MEX of [0,1,2,2,4] is 3.

Return the maximum MEX of nums after applying the mentioned operation any number of times.



Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] two times to make nums[1] = 0. The resulting array is nums = [1,0,7,13,6,8].
- The MEX of nums is 2. However, before calculating the MEX, you can apply the operation to other elements, possibly with additional operations, such that every element is changed.
- Here, you can also:
    - Subtract value from nums[2] once to make nums[2] = 2
    - Subtract value from nums[3] once to make nums[3] = 8
    - Subtract value from nums[4] once to make nums[4] = 1
- Resulting array: [1,0,2,8,1,8], The MEX is 3.
- If you apply these types of operations optimally, you can cover up to the maximum MEX 4.
Thus, the answer is 4.

Example 2:

Input: nums = [1,1,1,1,1], value = 1
Output: 5
Explanation: All elements can be made unique and cover [0,1,2,3,4] using the value = 1 operation, so the answer is 5.



Constraints:

- 1 <= nums.length, value <= 10^5
- -10^9 <= nums[i] <= 10^9

"""

from collections import Counter
from typing import List


class Solution:
    """
    Key idea:
    - The remainder of each number modulo `value` determines which numbers it can represent.
    - Count how many times each remainder appears (using Counter).
    - Then, starting from 0, for each candidate integer `n`, check if we still have an unused
      number with the same remainder (n % value). If not, `n` is the smallest missing integer.
    
    Complexity: O(len(nums)), since each number is processed once and each remainder check is O(1).
    """

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = Counter([n % value for n in nums])
        for n in range(len(nums) + 1):
            reminder = n % value
            if freq[reminder] == 0:
                return n
            freq[reminder] -= 1


import pytest


@pytest.mark.parametrize(
    "nums, value, expected",
    [
        ([1, -10, 7, 13, 6, 8], 5, 4),
    ],
)
def test_example_1(nums, value, expected):
    assert Solution().findSmallestInteger(nums, value) == expected


@pytest.mark.parametrize(
    "nums, value, expected",
    [
        ([1, 1, 1, 1, 1], 1, 5),
    ],
)
def test_example_2(nums, value, expected):
    assert Solution().findSmallestInteger(nums, value) == expected
