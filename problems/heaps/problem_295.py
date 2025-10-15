"""295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

* For example, for arr = [2,3,4], the median is 3.
* For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

* MedianFinder() initializes the MedianFinder object.
* void addNum(int num) adds the integer num from the data stream to the data structure.
* double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
* -10^5 <= num <= 10^5
* There will be at least one element in the data structure before calling findMedian.
* At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow up:
* If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
* If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""

import pytest
from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]

@pytest.fixture
def median_finder():
    return MedianFinder()


def test_example_1(median_finder):
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0


def test_single_number(median_finder):
    median_finder.addNum(5)
    assert median_finder.findMedian() == 5.0


def test_even_numbers(median_finder):
    median_finder.addNum(1)
    median_finder.addNum(2)
    median_finder.addNum(3)
    median_finder.addNum(4)
    assert median_finder.findMedian() == 2.5


def test_negative_numbers(median_finder):
    median_finder.addNum(-1)
    median_finder.addNum(-2)
    median_finder.addNum(-3)
    assert median_finder.findMedian() == -2.0


def test_duplicate_numbers(median_finder):
    median_finder.addNum(1)
    median_finder.addNum(1)
    median_finder.addNum(1)
    assert median_finder.findMedian() == 1.0
