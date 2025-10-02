"""
LeetCode Problem 239: Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

from collections import deque
from typing import List
import pytest


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = [0] * (len(nums) - k + 1)

        queue = deque()
        for n, val in enumerate(nums):
            left = n - k + 1
            if left < 0:
                left = 0

            # Remove the value that is to the left of the current window
            if queue and queue[0] < left:
                queue.popleft()

            # The values that are to the left of n and are no greater than val could not become new max
            while queue and nums[queue[-1]] <= val:
                queue.pop()

            queue.append(n)

            answer[left] = nums[queue[0]]

        return answer

    def maxSlidingWindow_deque(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        for n in range(k):
            val = nums[n]
            while queue and queue[-1][1] <= val:
                queue.pop()
            queue.append((n, val))

        answer = [queue[0][1]]

        for right in range(k, len(nums)):
            left = right - k + 1
            val = nums[right]

            if queue and queue[0][0] < left:
                queue.popleft()
            while queue and queue[-1][1] <= val:
                queue.pop()
            queue.append((right, val))

            answer.append(queue[0][1])

        return answer

    def maxSlidingWindow_semi_brute(self, nums: List[int], k: int) -> List[int]:
        curr_max = max(nums[0:k])
        answer = [curr_max]
        for n in range(1, len(nums) - k + 1):
            if nums[n + k - 1] >= curr_max:
                curr_max = nums[n + k - 1]
            elif nums[n - 1] < curr_max:
                pass
            else:
                curr_max = max(nums[n : n + k])
            answer.append(curr_max)
        return answer


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """
    Example 1: General case with k=3
    """
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [3, 3, 5, 5, 6, 7]
    assert sln.maxSlidingWindow(nums, k) == expected


def test_002(sln):
    """
    Example 2: Single element window
    """
    nums = [1]
    k = 1
    expected = [1]
    assert sln.maxSlidingWindow(nums, k) == expected


def test_003(sln):
    nums = [5, 4, 3]
    k = 2
    expected = [5, 4]
    assert sln.maxSlidingWindow(nums, k) == expected
