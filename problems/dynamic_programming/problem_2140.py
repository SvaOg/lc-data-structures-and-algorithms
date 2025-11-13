"""
2140. Solving Questions With Brainpower

You are given a 0-indexed 2D integer array questions where questions[i] = [points_i, brainpower_i].
The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you points_i points but you will be unable to solve each of the next brainpower_i questions. If you skip question i, you get to make the decision on the next question.
Return the maximum number of points you can earn for the exam.

Example 1:
Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve questions 1 and 2.
- Solve question 3: Earn 2 points. You will be unable to solve any more questions.
Total points earned: 3 + 2 = 5. There is no other strategy to earn 5 or more points.

Example 2:
Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 1 point, will be unable to solve questions 1.
- Solve question 3: Earn 4 points, will be unable to solve question 4.
Total points earned: 1 + 4 = 5.
Another strategy can be to solve question 1 and 4, earning 2 + 5 = 7 points. It is the maximum points you can earn.

Constraints:
1 <= questions.length <= 10^5
1 <= points_i, brainpower_i <= 10^5
"""

from typing import List
from functools import cache
import pytest

"""
Hint that worked - We store for each question the maximum points we can earn if we started the exam on that question.
"""


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        bottom-up solution beats 74%
        """
        n = len(questions)

        arr = [0] * (n + 1)  # to prevent going out of bounds
        for i in range(n - 1, -1, -1):
            j = min(i + questions[i][1] + 1, n)
            arr[i] = max(questions[i][0] + arr[j], arr[i + 1])

        return arr[0]

    def mostPoints_memo(self, questions: List[List[int]]) -> int:
        """
        Solution with memo is faster than one with cache (beats 34% vs 5%)
        """

        def dp(i):
            if i >= n:
                return 0
            if not i in memo:
                memo[i] = max(dp(i + 1), questions[i][0] + dp(i + questions[i][1] + 1))
            return memo[i]

        n = len(questions)
        memo = {}
        return dp(0)

    def mostPoints_cache(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= n:
                return 0
            return max(dp(i + 1), questions[i][0] + dp(i + questions[i][1] + 1))

        n = len(questions)
        return dp(0)


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    assert sln.mostPoints(questions) == 5


def test_002(sln):
    """Test the second example from the problem description."""
    questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    assert sln.mostPoints(questions) == 7


def test_003(sln):
    questions = [[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]
    expected = 157
    assert sln.mostPoints(questions) == expected
