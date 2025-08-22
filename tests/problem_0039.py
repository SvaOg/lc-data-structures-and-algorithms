"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

Follow up: What if the candidates array contains duplicates? How would you handle that?
"""

from turtle import back
from typing import List
import pytest


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, combo, curr_target):
            if curr_target == 0:
                results.append(list(combo))
                return

            for i in range(start, len(candidates)):
                value = candidates[i]
                if value > curr_target:
                    return
                combo.append(value)
                backtrack(i, combo, curr_target - value)
                combo.pop()

        results = []
        backtrack(0, [], target)
        return results


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    candidates = [2, 3, 6, 7]
    target = 7
    result = sln.combinationSum(candidates, target)
    assert sorted([sorted(combo) for combo in result]) == sorted(
        [sorted(combo) for combo in [[2, 2, 3], [7]]]
    )


def test_002(sln):
    """Test the second example from the problem description."""
    candidates = [2, 3, 5]
    target = 8
    result = sln.combinationSum(candidates, target)
    assert sorted([sorted(combo) for combo in result]) == sorted(
        [sorted(combo) for combo in [[2, 2, 2, 2], [2, 3, 3], [3, 5]]]
    )


def test_003(sln):
    """Test the third example from the problem description."""
    candidates = [2]
    target = 1
    result = sln.combinationSum(candidates, target)
    assert result == []
