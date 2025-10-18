"""
LeetCode Problem 433: Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is a mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid mutation.

Given the two gene strings startGene and endGene and the gene bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
Output: 2

Example 3:

Input: startGene = "AAAAACCC", endGene = "AACCCCCC", bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
Output: 3
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def diff(s1, s2):
            return sum(1 if ord(ch1) - ord(ch2) != 0 else 0 for ch1, ch2 in zip(s1, s2))

        bank.append(startGene)

        graph = defaultdict(list)
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                if diff(bank[i], bank[j]) == 1:
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])

        if endGene not in bank:
            return -1

        queue = deque()
        seen = set()

        queue.append((startGene, 0))
        seen.add(startGene)

        while queue:
            node, steps = queue.popleft()
            if node == endGene:
                return steps

            for neighbor in graph[node]:
                if neighbor not in seen:
                    queue.append((neighbor, steps + 1))
                    seen.add(neighbor)

        return -1


# Test cases based on the examples
import pytest


@pytest.mark.parametrize(
    "startGene, endGene, bank, expected",
    [
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
    ],
)
def test_example1(startGene, endGene, bank, expected):
    assert Solution().minMutation(startGene, endGene, bank) == expected


@pytest.mark.parametrize(
    "startGene, endGene, bank, expected",
    [
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
    ],
)
def test_example2(startGene, endGene, bank, expected):
    assert Solution().minMutation(startGene, endGene, bank) == expected


@pytest.mark.parametrize(
    "startGene, endGene, bank, expected",
    [
        ("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3),
    ],
)
def test_example3(startGene, endGene, bank, expected):
    assert Solution().minMutation(startGene, endGene, bank) == expected
