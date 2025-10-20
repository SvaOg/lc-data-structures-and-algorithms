"""
480. Sliding Window Median
https://leetcode.com/problems/sliding-window-median/

The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Given an integer array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the median array for each window in the original array. Answers within 10^-5 of the actual value will be accepted.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.0,-1.0,-1.0,3.0,5.0,6.0]
Explanation:
Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6

Example 2:
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.0,3.0,3.0,3.0,2.0,3.0,2.0]

Constraints:
* 1 <= k <= nums.length <= 10^5
* -2^31 <= nums[i] <= 2^31 - 1
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class MedianFinder:
    """
    A data structure that maintains the median of a sliding window of size k.
    Uses two heaps (max heap for smaller half, min heap for larger half) with lazy deletion.
    """

    def __init__(self, k: int):
        """
        Initialize the MedianFinder with window size k.

        Args:
            k: The size of the sliding window
        """
        self.k = k
        # Max heap for smaller half (negated values for max heap behavior)
        self.small = []
        # Min heap for larger half
        self.large = []
        # Track elements to be lazily deleted with their counts
        self.delayed = defaultdict(int)
        # Actual size of elements in small heap (excluding delayed deletions)
        self.small_size = 0
        # Actual size of elements in large heap (excluding delayed deletions)
        self.large_size = 0

    def add_num(self, num: int) -> None:
        """
        Add a number to the data structure.

        Args:
            num: The number to add
        """
        # Determine which heap to add the number to
        if not self.small or num <= -self.small[0]:
            # Add to small heap (negate for max heap behavior)
            heappush(self.small, -num)
            self.small_size += 1
        else:
            # Add to large heap
            heappush(self.large, num)
            self.large_size += 1

        # Ensure heaps remain balanced
        self.rebalance()

    def find_median(self) -> float:
        """
        Find the median of current elements in the window.

        Returns:
            The median value as a float
        """
        # If k is odd, median is the top of small heap
        # If k is even, median is average of tops of both heaps
        return -self.small[0] if self.k & 1 else (-self.small[0] + self.large[0]) / 2

    def remove_num(self, num: int) -> None:
        """
        Remove a number from the data structure using lazy deletion.

        Args:
            num: The number to remove
        """
        # Mark the number for lazy deletion
        self.delayed[num] += 1

        # Update size and prune if the number is at the top
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self.prune(self.large)

        # Ensure heaps remain balanced
        self.rebalance()

    def prune(self, heap: List[int]) -> None:
        """
        Remove all delayed elements from the top of the heap.

        Args:
            heap: The heap to prune (either self.small or self.large)
        """
        # Determine sign for value conversion (-1 for small heap, 1 for large heap)
        sign = -1 if heap is self.small else 1

        # Remove all delayed elements from the top
        while heap and sign * heap[0] in self.delayed:
            # Decrease the delay count
            self.delayed[sign * heap[0]] -= 1
            # Remove from delayed dict if count reaches 0
            if self.delayed[sign * heap[0]] == 0:
                self.delayed.pop(sign * heap[0])
            # Remove from heap
            heappop(heap)

    def rebalance(self) -> None:
        """
        Rebalance the two heaps to maintain the median property.
        Small heap should have equal or one more element than large heap.
        """
        # If small heap has too many elements, move one to large heap
        if self.small_size > self.large_size + 1:
            heappush(self.large, -heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
            # Clean up any delayed elements exposed at the top
            self.prune(self.small)
        # If large heap has more elements, move one to small heap
        elif self.small_size < self.large_size:
            heappush(self.small, -heappop(self.large))
            self.large_size -= 1
            self.small_size += 1
            # Clean up any delayed elements exposed at the top
            self.prune(self.large)


class Solution:
    """
    Solution for the Sliding Window Median problem.
    """

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Find the median of each sliding window of size k in the array.

        Args:
            nums: The input array of numbers
            k: The size of the sliding window

        Returns:
            List of medians for each window position
        """
        # Initialize the median finder with window size k
        finder = MedianFinder(k)

        # Add the first k elements to initialize the window
        for num in nums[:k]:
            finder.add_num(num)

        # Calculate the median for the first window
        result = [finder.find_median()]

        # Slide the window through the rest of the array
        for i in range(k, len(nums)):
            # Add new element entering the window
            finder.add_num(nums[i])
            # Remove element leaving the window
            finder.remove_num(nums[i - k])
            # Calculate and store the median for current window
            result.append(finder.find_median())

        return result


def test_example_01():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    output = Solution().medianSlidingWindow(nums, k)
    assert output == expected


def test_example_02():
    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k = 3
    expected = [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
    output = Solution().medianSlidingWindow(nums, k)
    assert output == expected
