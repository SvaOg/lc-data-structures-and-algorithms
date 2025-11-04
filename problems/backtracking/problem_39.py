"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/description/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is a candidate, and 7 = 7. These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 2 + 2 = 8. 2 and 3 are candidates, and 2 + 3 + 3 = 8. 3 and 5 are candidates, and 3 + 5 = 8.

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

from typing import List
import pytest


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(combo, idx, curr_target):
            if curr_target == 0:
                result.append(combo[:])
                return

            for i in range(idx, n):
                v = candidates[i]
                if v > curr_target:
                    return
                combo.append(v)
                backtrack(combo, i, curr_target - v)
                combo.pop()

        candidates.sort()
        n = len(candidates)
        result = []

        backtrack([], 0, target)

        return result


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    candidates = [2, 3, 6, 7]
    target = 7
    assert sln.combinationSum(candidates, target) == [[2, 2, 3], [7]]


def test_002(sln):
    """Test the second example from the problem description."""
    candidates = [2, 3, 5]
    target = 8
    assert sln.combinationSum(candidates, target) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_003(sln):
    """Test the third example from the problem description."""
    candidates = [2]
    target = 1
    assert sln.combinationSum(candidates, target) == []
