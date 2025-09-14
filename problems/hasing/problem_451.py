"""
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' should appear before 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "cccaaa"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        group_by_freq = defaultdict(list)
        for ch, fr in Counter(s).items():
            group_by_freq[fr].append(ch)

        ans = []

        for fr in sorted(group_by_freq.keys(), reverse=True):
            for ch in sorted(group_by_freq[fr]):
                ans.extend([ch] * fr)

        return "".join(ans)

    def frequencySort1(self, s: str) -> str:
        freq = Counter(s)
        return "".join(sorted(s, key=freq.get, reverse=True))

    def frequencySort2(self, s: str) -> str:
        freq = [(fr, ch) for ch, fr in Counter(s).items()]

        ans = []
        for fr, ch in sorted(freq, reverse=True):
            ans.extend([ch] * fr)


def test_example_1():
    solution = Solution()
    assert solution.frequencySort("tree") in ["eert", "eetr"]


def test_example_2():
    solution = Solution()
    assert solution.frequencySort("cccaaa") in ["cccaaa", "aaaccc"]


def test_example_3():
    solution = Solution()
    assert solution.frequencySort("Aabb") in ["bbAa", "bbaA"]


def test_example_4():
    solution = Solution()
    assert solution.frequencySort("loveleetcode") in [
        "eeeelloocdtv",
    ]
