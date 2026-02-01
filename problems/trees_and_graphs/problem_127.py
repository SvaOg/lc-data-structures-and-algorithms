"""
LeetCode Problem 127: Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, so we cannot form a transformation sequence.

Example 3:

Input: beginWord = "a", endWord = "c", wordList = ["a","b","c"]
Output: 2
Explanation: "a" -> "c".
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Optimized solution using Breadth-First Search (BFS).

        The key optimization is in how 'one-step' neighbors are found,
        avoiding the O(N^2 * L) pair-wise word comparison of the original solution.

        1. Graph Construction (Preprocessing):
           - The graph is implicitly built using an 'Adjacency Map' (graph/defaultdict).
           - Keys are 'wildcard patterns' (e.g., "h*t") and values are sets of words
             that match that pattern (e.g., {"hit", "hot"}).
           - This pre-calculation takes O(N * L^2) time (N words, L length, L patterns per word).
           - Any two words sharing a pattern are connected, achieving the same result as
             the O(N^2) comparison much faster.

        2. BFS Traversal:
           - The neighbors() function finds all words sharing *any* pattern with the
             current word by looking up the word's L patterns in the graph map.
           - This neighbor lookup is O(L) time.
           - The overall BFS time complexity is closer to O(N * L) for traversing all
             nodes/edges, resulting in a much faster total runtime.
        """

        def patterns(word):
            arr = [ch for ch in word]

            patterns = []
            for i in range(len(word)):
                ch, arr[i] = arr[i], "*"
                patterns.append("".join(arr))
                arr[i] = ch

            return patterns

        def neighbors(word):
            words = []
            for pattern in patterns(word):
                words.extend(graph[pattern])
            return words

        graph = defaultdict(set)
        found = False

        wordList.append(beginWord)

        for i in range(len(wordList)):
            word = wordList[i]
            if word == endWord:
                found = True
            for pattern in patterns(word):
                graph[pattern].add(word)

        if not found:
            return 0

        queue = deque([(beginWord, 1)])
        seen = set([beginWord])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            for next_word in neighbors(word):
                if next_word not in seen:
                    seen.add(next_word)
                    queue.append((next_word, steps + 1))

        return 0

    def ladderLength_TLE(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        def distance(word1, word2):
            return sum(
                1 if ord(ch2) - ord(ch1) != 0 else 0 for ch1, ch2 in zip(word1, word2)
            )

        wordList.append(beginWord)

        n = len(wordList)

        graph = defaultdict(list)
        for i in range(n):
            word1 = wordList[i]
            for j in range(i + 1, n):
                word2 = wordList[j]
                if distance(word1, word2) == 1:
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        if endWord not in graph:
            return 0

        queue = deque([(beginWord, 1)])
        seen = set([beginWord])

        while queue:
            node, steps = queue.popleft()
            if node == endWord:
                return steps

            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return 0


import pytest


def test_example1():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected = 5
    assert Solution().ladderLength(beginWord, endWord, wordList) == expected


@pytest.mark.parametrize(
    "beginWord, endWord, wordList, expected",
    [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ],
)
def test_example2(beginWord, endWord, wordList, expected):
    assert Solution().ladderLength(beginWord, endWord, wordList) == expected


@pytest.mark.parametrize(
    "beginWord, endWord, wordList, expected",
    [
        ("a", "c", ["a", "b", "c"], 2),
    ],
)
def test_example3(beginWord, endWord, wordList, expected):
    assert Solution().ladderLength(beginWord, endWord, wordList) == expected
