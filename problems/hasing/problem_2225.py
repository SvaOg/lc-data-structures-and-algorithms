"""
LeetCode Problem 2225: Find Players With Zero or One Losses

You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:
- answer[0] is a list of all players that have not lost any matches.
- answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

Constraints:
- 1 <= matches.length <= 10^5
- matches[i].length == 2
- 1 <= winneri, loseri <= 10^5
- winneri != loseri
"""

from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        more_losses = set()

        for winner, looser in matches:
            if winner not in one_loss and winner not in more_losses:
                zero_loss.add(winner)

            if looser in zero_loss:
                zero_loss.remove(looser)
                one_loss.add(looser)
            elif looser in one_loss:
                one_loss.remove(looser)
                more_losses.add(looser)
            elif looser in more_losses:
                continue
            else:
                one_loss.add(looser)

        return [sorted(zero_loss), sorted(one_loss)]

    def findWinners2(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        for winner, looser in matches:
            losses.setdefault(winner, [0])
            losses.setdefault(looser, [0])[0] += 1

        answer = [[], []]
        for player, [num_losses] in sorted(losses.items()):
            if num_losses < 2:
                answer[num_losses].append(player)

        return answer


def test_findWinners():
    solution = Solution()

    # Test case 1
    matches1 = [
        [1, 3],
        [2, 3],
        [3, 6],
        [5, 6],
        [5, 7],
        [4, 5],
        [4, 8],
        [4, 9],
        [10, 4],
        [10, 9],
    ]
    expected1 = [[1, 2, 10], [4, 5, 7, 8]]
    assert solution.findWinners(matches1) == expected1

    # Test case 2
    matches2 = [[2, 3], [1, 3], [5, 4], [6, 4]]
    expected2 = [[1, 2, 5, 6], []]
    assert solution.findWinners(matches2) == expected2
