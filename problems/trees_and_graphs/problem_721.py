"""
721. Accounts Merge

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: accounts = [["John","johnsmith@mail.com","john00@mail.com"],["John","johnnybravo@mail.com"],["John","johnsmith@mail.com","john_newyork@mail.com"],["Mary","mary@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["John","johnnybravo@mail.com"],["Mary","mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email address.
"""

from collections import defaultdict
from typing import List, Optional
import pytest


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> Optional[List[List[str]]]:
        graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                graph[first_email].append(email)
                graph[email].append(first_email)

        visited = set()
        merged_accounts = []

        for email in graph:
            if email in visited:
                continue

            visited.add(email)

            component = [email]
            stack = [email]

            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        component.append(neighbor)
                        stack.append(neighbor)

            merged_accounts.append([email_to_name[email]] + sorted(component))

        return merged_accounts


class Solution1:
    def accountsMerge(self, accounts: List[List[str]]) -> Optional[List[List[str]]]:
        # Here I'll be keeping a list of indexes for each encountered email
        emails: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
        # Emails represent the nodes in the graph. This is adjecency list for this graph.
        graph: defaultdict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                first_email_key = (i, 1)

                this_email = accounts[i][j]
                this_email_key = (i, j)

                graph[this_email_key] = []
                emails[this_email].append(this_email_key)

                # Connect this occurence of email to all existing accounts where it is present
                for key in emails[this_email]:
                    if key != this_email_key:
                        graph[this_email_key].append(key)
                        graph[key].append(this_email_key)

                if this_email_key != first_email_key:
                    graph[first_email_key].append(this_email_key)
                    graph[this_email_key].append(first_email_key)

        seen: set[tuple[int, int]] = set()

        def dfs(node, current_account):
            current_account.add(accounts[node[0]][node[1]])
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor, current_account)

        answer = []

        for email_key in graph:
            if email_key in seen:
                continue

            account_name = accounts[email_key[0]][0]

            current_account_emails = set()
            dfs(email_key, current_account_emails)

            answer.append([account_name] + list(sorted(current_account_emails)))

        return answer


@pytest.fixture
def sln():
    yield Solution()


def test_001(sln):
    """Test the first example from the problem description."""
    accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"],
    ]
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["Mary", "mary@mail.com"],
    ]
    # Sort both for comparison as order of accounts does not matter
    result = sln.accountsMerge(accounts)
    if result:
        result.sort()
        expected.sort()
    assert result == expected


def test_002(sln):
    """Test the second example from the problem description."""
    accounts = [
        ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
        ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
        ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
        ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
        ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
    ]
    expected = [
        ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
        ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
        ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
        ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
        ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
    ]
    # Sort both for comparison as order of accounts does not matter
    result = sln.accountsMerge(accounts)
    if result:
        result.sort()
        expected.sort()
    assert result == expected


def test_003(sln):
    """Test the second example from the problem description."""

    accounts = [
        ["David", "David0@m.co", "David1@m.co"],
        ["David", "David3@m.co", "David4@m.co"],
        ["David", "David4@m.co", "David5@m.co"],
        ["David", "David2@m.co", "David3@m.co"],
        ["David", "David1@m.co", "David2@m.co"],
    ]

    expected = [
        [
            "David",
            "David0@m.co",
            "David1@m.co",
            "David2@m.co",
            "David3@m.co",
            "David4@m.co",
            "David5@m.co",
        ]
    ]

    # Sort both for comparison as order of accounts does not matter
    result = sln.accountsMerge(accounts)
    if result:
        result.sort()
        expected.sort()
    assert result == expected
