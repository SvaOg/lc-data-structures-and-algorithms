"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

from typing import List
import pytest


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        n = len(digits)
        subst = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(digit_idx, combo):
            if len(combo) == n:
                result.append("".join(combo))
                return
            for ch in subst[digits[digit_idx]]:
                combo.append(ch)
                backtrack(digit_idx + 1, combo)
                combo.pop()

        result = []
        backtrack(0, [])
        return result


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    digits = "23"
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sln.letterCombinations(digits) == expected


def test_002(sln):
    """Test the second example from the problem description."""
    digits = ""
    expected: List[str] = []
    assert sln.letterCombinations(digits) == expected


def test_003(sln):
    """Test the third example from the problem description."""
    digits = "2"
    expected = ["a", "b", "c"]
    assert sln.letterCombinations(digits) == expected
