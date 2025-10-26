"""
1283. Find the Smallest Divisor Given a Threshold

Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum up the result of the division. We will use the result of each division rounded up to the nearest integer.

Return the smallest divisor such that the result mentioned above is less than or equal to threshold.

The test cases are generated so that there will be an answer.

Example 1:
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: If the divisor is 5, the result is ceil(1/5) + ceil(2/5) + ceil(5/5) + ceil(9/5) = 1 + 1 + 1 + 2 = 5 which is less than or equal to 6.
If the divisor is 4, the result is 1 + 1 + 2 + 3 = 7, which is greater than 6.

Example 2:
Input: nums = [44,22,33,11,1], threshold = 5
Output: 44
Explanation: The smallest divisor is 44 because ceil(44/44)+ceil(22/44)+ceil(33/44)+ceil(11/44)+ceil(1/44) = 1+1+1+1+1 = 5.

Example 3:
Input: nums = [21212,10101,12121], threshold = 1000000
Output: 1
Explanation: The sum is already <= threshold when the divisor is 1.

Constraints:
1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
1 <= threshold <= 10^6
"""

from math import ceil
from typing import List
import pytest


class Solution:
    """
    Binary search on solution space.
    The solution where check was provided as a separate function TLEd.
    This variant worked.
    """

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left <= right:
            candidate = (left + right) // 2

            sum = 0
            for n in nums:
                sum += (n + candidate - 1) // candidate

            if sum <= threshold:
                right = candidate - 1
            else:
                left = candidate + 1

        return left


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    nums = [1, 2, 5, 9]
    threshold = 6
    assert sln.smallestDivisor(nums, threshold) == 5


def test_002(sln):
    """Test the second example from the problem description."""
    nums = [44, 22, 33, 11, 1]
    threshold = 5
    assert sln.smallestDivisor(nums, threshold) == 44


def test_003(sln):
    """Test the third example from the problem description."""
    nums = [21212, 10101, 12121]
    threshold = 1_000_000
    assert sln.smallestDivisor(nums, threshold) == 1


def test_004(sln):
    """Test the third example from the problem description."""
    nums = [12, 50, 11, 75, 57, 12, 73, 4, 69, 78]
    threshold = 649
    assert sln.smallestDivisor(nums, threshold) == 1


def test_005(sln):
    nums = [
        22045,
        35424,
        13308,
        96671,
        8022,
        96779,
        77550,
        71927,
        59321,
        51672,
        88521,
        81462,
        73175,
        1038,
        56268,
        24501,
        81587,
        19494,
        75837,
        97672,
        61173,
        19557,
        48784,
        24980,
        38950,
        76121,
        73473,
        23175,
        11929,
        46196,
        79147,
        26757,
        95971,
        53617,
        23266,
        21099,
        86613,
        37881,
        11355,
        3070,
        74936,
        36518,
        95563,
        48886,
        24159,
        90467,
        25780,
        68883,
        37058,
        98820,
        72247,
        20346,
        27093,
        9139,
        52670,
        23473,
        75683,
        75072,
        42013,
        31041,
        94427,
        4791,
        76061,
        54177,
        58577,
        51578,
        42203,
        82082,
        98319,
        526,
        69847,
        12628,
        27702,
        25691,
        62698,
        30872,
        35111,
        25642,
        9662,
        39343,
        72585,
        53465,
        43977,
        98401,
        10171,
        47736,
        51467,
        72451,
        45498,
        19869,
        31112,
        43385,
        63396,
        44296,
        21839,
        24441,
        81227,
        68618,
        84543,
        28002,
    ]
    threshold = 3256
    assert sln.smallestDivisor(nums, threshold) == 1539
