"""
399. Evaluate Division

You are given a list of equations and their corresponding values. Equations are in the format: a / b = value, where a and b are variables represented by strings, and value is a floating-point number. You are also given some queries, where each query is in the format: c / d.

Return the answers to all queries. If an answer does not exist, return -1.0 for that query.

Note:
- The input is always valid. You may assume that evaluating the queries will not result in division by zero, and there is no contradiction.
- The variables used in the input are defined and appear in at least one equation.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
Queries:
a / c = a / b * b / c = 2.0 * 3.0 = 6.0
b / a = 1 / (a / b) = 1 / 2.0 = 0.5
a / e = -1.0 (as 'e' is not in the equations)
a / a = 1.0
x / x = -1.0 (as 'x' is not in the equations)

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
- 1 <= equations.length <= 20
- equations[i].length == 2
- 1 <= a, b, c, d <= 5 where a, b, c, d are lowercase English letters or arbitrary variable names
- 0.0 < values[i] <= 20.0
- 1 <= queries.length <= 20
- queries[i].length == 2
- a, b, c, d are variables that appear in the input or are new variables
"""

from collections import deque
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}
        for (var1, var2), val in zip(equations, values):
            graph.setdefault(var1, {}).update({var2: val})
            graph.setdefault(var2, {}).update({var1: 1.0 / val})

        def dfs(start, end):
            if start not in graph or end not in graph:
                return -1
            if start == end:
                return 1

            stack = [(start, 1)]
            seen = set([start])

            while stack:
                node, ratio = stack.pop()
                if node == end:
                    return ratio

                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, ratio * graph[node][neighbor]))

            return -1

        return [dfs(v1, v2) for v1, v2 in queries]


# Pytest test cases

import pytest


def test_example1():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    ans = Solution().calcEquation(equations, values, queries)
    assert pytest.approx(ans) == expected


def test_example2():
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expected = [3.75000, 0.40000, 5.00000, 0.20000]
    ans = Solution().calcEquation(equations, values, queries)
    assert pytest.approx(ans) == expected


def test_example3():
    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected = [0.50000, 2.00000, -1.00000, -1.00000]
    ans = Solution().calcEquation(equations, values, queries)
    assert pytest.approx(ans) == expected
