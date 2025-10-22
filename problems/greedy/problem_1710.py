"""
1710. Maximum Units on a Truck

You are assigned to put some boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

- numberOfBoxesi is the number of boxes of type i.
- numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of type [1,3] = 3 units.
- 2 boxes of type [2,2] = 2 * 2 = 4 units.
- 3 boxes of type [3,1] = 3 * 1 = 3 units.
You can take all the boxes of the first and second type, and one box of the third type.
The total number of units = 1*3 + 2*2 + 1*1 = 3 + 4 + 1 = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Constraints:
- 1 <= boxTypes.length <= 1000
- 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
- 1 <= truckSize <= 10^6
"""

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda v: v[1], reverse=True)

        total_units, space_left = 0, truckSize

        for num_boxes, num_units in boxTypes:
            boxes_to_load = num_boxes if num_boxes <= space_left else space_left
            space_left -= boxes_to_load
            total_units += num_units * boxes_to_load
            if space_left == 0:
                break

        return total_units


import pytest


def test_example1():
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    expected = 8
    assert Solution().maximumUnits(boxTypes, truckSize) == expected


def test_example2():
    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10
    expected = 91
    assert Solution().maximumUnits(boxTypes, truckSize) == expected
