"""
1436. Destination City
https://leetcode.com/problems/destination-city/

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" -> "New York" -> "Lima" -> "Sao Paulo". "Sao Paulo" has no outgoing paths.

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: "D" -> "B" -> "C" -> "A". "A" has no outgoing paths.

Example 3:
Input: paths = [["A","Z"]]
Output: "Z"

Constraints:
- 1 <= paths.length <= 100
- paths[i].length == 2
- 1 <= cityAi.length, cityBi.length <= 10
- cityAi != cityBi
- All strings consist of lowercase and uppercase English letters and the space character.

"""

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return list(set(dst for _, dst in paths) - set(src for src, _ in paths))[0]


import pytest


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    assert solution.destCity(paths) == "Sao Paulo"


def test_example_2(solution):
    paths = [["B", "C"], ["D", "B"], ["C", "A"]]
    assert solution.destCity(paths) == "A"


def test_example_3(solution):
    paths = [["A", "Z"]]
    assert solution.destCity(paths) == "Z"
