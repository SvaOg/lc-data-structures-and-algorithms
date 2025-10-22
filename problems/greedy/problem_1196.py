"""
1196. How Many Apples Can You Put into the Basket

You have some apples, where arr[i] is the weight of the i-th apple. You can choose any number of apples to put into a basket.
The weight of the basket must be less than or equal to 5000.

Return the maximum number of apples you can put in the basket.

Example 1:
Input: arr = [100,200,150,1000]
Output: 4
Explanation: All 4 apples can be carried, and their total weight is 100 + 200 + 150 + 1000 = 1450 < 5000.

Example 2:
Input: arr = [900,950,800,1000,700,800]
Output: 5
Explanation: There are 6 apples, choose the lightest 5 for a total weight of 700 + 800 + 800 + 900 + 950 = 4150 < 5000.

Constraints:
- 1 <= arr.length <= 10^3
- 1 <= arr[i] <= 10^3
"""

from typing import List


class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        count = 0
        arr.sort()
        n, space_left = 0, 5000
        while n < len(arr) and space_left > 0:
            apple = arr[n]
            n += 1
            if space_left >= apple:
                count += 1
                space_left -= apple
        return count


import pytest


def test_example1():
    arr = [100, 200, 150, 1000]
    expected = 4
    assert Solution().maxNumberOfApples(arr) == expected


def test_example2():
    arr = [900, 950, 800, 1000, 700, 800]
    expected = 5
    assert Solution().maxNumberOfApples(arr) == expected
