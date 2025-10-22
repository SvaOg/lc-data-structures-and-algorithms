"""
1323. Maximum 69 Number

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 9969.
Changing the second digit results in 9699.
Changing the third digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation:
Changing the last digit 6 to 9 results in 9999.

Example 3:
Input: num = 9999
Output: 9999
Explanation:
It is better not to change any digit.

Constraints:
- 1 <= num <= 10^4
- num consists of only 6 and 9 digits.
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        arr = [ch for ch in str(num)]
        for i in range(len(arr)):
            if arr[i] == "6":
                arr[i] = "9"
                break
        else:
            return num
        return int("".join(arr))


import pytest


def test_example1():
    num = 9669
    expected = 9969
    assert Solution().maximum69Number(num) == expected


def test_example2():
    num = 9996
    expected = 9999
    assert Solution().maximum69Number(num) == expected


def test_example3():
    num = 9999
    expected = 9999
    assert Solution().maximum69Number(num) == expected
