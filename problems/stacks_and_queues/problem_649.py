"""
LeetCode Problem 649: Dota2 Senate

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

1. Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
2. Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party respectively. Then if there are n senators, the round-based procedure starts from the first senator to the nth senator in order, and the procedure will last until a party announces victory.

Given the string senate, return "Radiant" if the Radiant party wins and "Dire" if the Dire party wins.

Example 1:
Input: senate = "RD"
Output: "Radiant"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And in the end, the first senator can announce the victory and make the decision.

Example 2:
Input: senate = "RDD"
Output: "Dire"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And the third senator comes from Dire and he can ban the first senator's right in the round 2.
And in the end, the third senator can announce the victory and make the decision.

Constraints:
- n == senate.length
- 1 <= n <= 10^4
- senate[i] is either 'R' or 'D'.
"""

from collections import Counter, deque


class Solution:
    """
    The idea - fUse a queue to store them. Now starting from the front of the queue, say its R,
    if we have not encountered any D before, we will pop and simply push the R in the back of the queue
    and increment the count of R encountered. But if we have encountered any D before, we will
    just pop the R and decrease the count of D.
    """

    def predictPartyVictory(self, senate: str) -> str:
        counts = Counter(senate)
        voting = deque(senate)
        votes = {"R": 0, "D": 0}

        winner = None
        while True:
            senator = voting.popleft()

            other_party = "D" if senator == "R" else "R"
            if counts[other_party] == 0:
                winner = "Radiant" if senator == "R" else "Dire"
                break

            if votes[other_party]:
                votes[other_party] -= 1
                counts[senator] -= 1
            else:
                votes[senator] += 1
                voting.append(senator)

        return winner


import pytest


def test_example_1():
    """
    Example 1:
    Input: senate = "RD"
    Output: "Radiant"
    """
    sol = Solution()
    assert sol.predictPartyVictory("RD") == "Radiant"


def test_example_2():
    """
    Example 2:
    Input: senate = "RDD"
    Output: "Dire"
    """
    sol = Solution()
    assert sol.predictPartyVictory("RDD") == "Dire"
