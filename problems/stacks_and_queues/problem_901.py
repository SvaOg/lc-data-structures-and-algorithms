"""
LeetCode Problem 901: Online Stock Span

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the price of the stock was less than or equal to today's price.

- For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].

Implement the StockSpanner class:

- StockSpanner() Initializes the object of the class.
- int next(int price) Returns the span of the stock's price given that today's price is price.

Example 1:
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4
stockSpanner.next(85);  // return 6

Constraints:
- 1 <= price <= 10^5
- At most 10^4 calls will be made to next.
"""


class StockSpanner:
    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        count = 1
        while self.stock and self.stock[-1][0] <= price:
            count += self.stock.pop()[1]
        self.stock.append((price, count))
        return count


import pytest


def test_example_1():
    """
    Example 1:
    Input
    ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    [[], [100], [80], [60], [70], [60], [75], [85]]
    Output
    [null, 1, 1, 1, 2, 1, 4, 6]
    """
    stockSpanner = StockSpanner()
    assert stockSpanner.next(100) == 1
    assert stockSpanner.next(80) == 1
    assert stockSpanner.next(60) == 1
    assert stockSpanner.next(70) == 2
    assert stockSpanner.next(60) == 1
    assert stockSpanner.next(75) == 4
    assert stockSpanner.next(85) == 6
