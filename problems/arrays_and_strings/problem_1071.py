"""
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/

For two strings s and t, we say "t divides s" if and only if
s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or
more times to form s).

Given two strings str1 and str2, return the largest string x such that x
divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.
"""

import pytest
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        divisors = self.get_common_divisors(n1, n2)

        greatest_divisor = ""
        for i in divisors:
            candidate = str1[:i]
            if (
                "".join([candidate] * (n1 // i)) == str1
                and "".join([candidate] * (n2 // i)) == str2
            ):
                greatest_divisor = candidate

        return greatest_divisor

    def get_common_divisors(self, m, n):
        # 1. Find the Greatest Common Divisor
        # Time Complexity: O(log(min(m, n)))
        gcd_val = math.gcd(m, n)

        divisors = []

        # 2. Find all divisors of the GCD up to its square root
        # Time Complexity: O(sqrt(GCD))
        limit = int(math.isqrt(gcd_val))

        for i in range(1, limit + 1):
            if gcd_val % i == 0:
                divisors.append(i)
                # If the divisor isn't the square root, add the paired divisor
                if i * i != gcd_val:
                    divisors.append(gcd_val // i)

        # 3. Sort the list (The list of divisors is small, so this is fast)
        divisors.sort()
        return divisors


@pytest.fixture
def sln():
    yield Solution()


# @pytest.mark.xfail(reason="Not implemented", strict=True)
def test_001(sln):
    """ABCABC and ABC have GCD string ABC."""
    assert sln.gcdOfStrings("ABCABC", "ABC") == "ABC"


def test_002(sln):
    """ABABAB and ABAB have GCD string AB."""
    assert sln.gcdOfStrings("ABABAB", "ABAB") == "AB"


def test_003(sln):
    """LEET and CODE have no common divisor string."""
    assert sln.gcdOfStrings("LEET", "CODE") == ""
