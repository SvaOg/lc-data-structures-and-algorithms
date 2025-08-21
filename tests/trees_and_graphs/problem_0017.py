"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

2: "abc"
3: "def"
4: "ghi"
5: "jkl"
6: "mno"
7: "pqrs"
8: "tuv"
9: "wxyz"

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

Follow up: Can you solve this problem using backtracking?
"""

from typing import List
import pytest


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(path, idx):
            if idx == len(digits):
                result.append(path)
                return

            for letter in phone[digits[idx]]:
                backtrack(path + letter, idx + 1)

        result = []
        if digits:
            backtrack("", 0)
        return result


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    digits = "23"
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    result = sln.letterCombinations(digits)
    assert len(result) == len(expected)
    for combination in expected:
        assert combination in result


def test_002(sln):
    """Test the second example from the problem description."""
    digits = ""
    assert sln.letterCombinations(digits) == []


def test_003(sln):
    """Test the third example from the problem description."""
    digits = "2"
    expected = ["a", "b", "c"]
    result = sln.letterCombinations(digits)
    assert len(result) == len(expected)
    for combination in expected:
        assert combination in result


def test_single_digit_9(sln):
    """Test with single digit 9."""
    digits = "9"
    expected = ["w", "x", "y", "z"]
    result = sln.letterCombinations(digits)
    assert len(result) == len(expected)
    for combination in expected:
        assert combination in result


def test_two_digits_79(sln):
    """Test with two digits 79."""
    digits = "79"
    expected = [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz",
    ]
    result = sln.letterCombinations(digits)
    assert len(result) == len(expected)
    for combination in expected:
        assert combination in result


def test_three_digits_234(sln):
    """Test with three digits 234."""
    digits = "234"
    result = sln.letterCombinations(digits)
    # 3 * 3 * 3 = 27 combinations
    assert len(result) == 27
    # Check that all combinations are valid
    for combination in result:
        assert len(combination) == 3
        assert combination[0] in "abc"
        assert combination[1] in "def"
        assert combination[2] in "ghi"
