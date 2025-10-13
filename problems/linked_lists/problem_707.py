"""
707. Design Linked List
https://leetcode.com/problems/design-linked-list/

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example 1:
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

Constraints:
- 0 <= index, val <= 1000
- Please do not use the built-in LinkedList library.
- At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""

import pytest


class MyLinkedList:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

        def __repr__(self):
            return f"ListNode({self.val})"

    def __init__(self):
        self.dummy1 = MyLinkedList.ListNode(0)
        self.size = 0
        pass

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy1.next
        while index:
            curr = curr.next
            index -= 1
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = MyLinkedList.ListNode(val)
        new_node.next = self.dummy1.next
        self.dummy1.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.dummy1.next is None:
            self.dummy1.next = MyLinkedList.ListNode(val)
        else:
            curr = self.dummy1.next
            while curr.next:
                curr = curr.next
            curr.next = MyLinkedList.ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > len(self):
            return

        if index == 0:
            self.addAtHead(val)
        elif index == len(self):
            self.addAtTail(val)
        else:
            pos = self.dummy1
            while index > 0:
                pos = pos.next
                index -= 1
            pos.next, pos.next.next = MyLinkedList.ListNode(val), pos.next
            self.size += 1

        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= len(self):
            return

        if index == 0:
            self.dummy1.next = self.dummy1.next.next
            self.size -= 1
        else:
            prev, pos = None, self.dummy1
            while index > -1:
                prev, pos = pos, pos.next
                index -= 1
            prev.next = pos.next
            self.size -= 1

    def toArray(self):
        res = []
        curr = self.dummy1.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    def __len__(self) -> int:
        return self.size


@pytest.fixture
def list1():
    my_list = MyLinkedList()
    my_list.addAtHead(3)
    my_list.addAtHead(2)
    my_list.addAtHead(1)
    return my_list


def test_001():
    my_list = MyLinkedList()
    my_list.addAtHead(3)
    my_list.addAtHead(2)
    my_list.addAtHead(1)
    assert my_list.toArray() == [1, 2, 3]


def test_002(list1):
    assert list1.get(0) == 1
    assert list1.get(2) == 3
    assert list1.get(3) == -1
    assert list1.get(-1) == -1


def test_003(list1):
    assert len(list1) == 3
    assert len(MyLinkedList()) == 0


def test_004():
    my_list = MyLinkedList()
    my_list.addAtTail(1)
    my_list.addAtTail(2)
    my_list.addAtTail(3)
    assert len(my_list) == 3
    assert my_list.toArray() == [1, 2, 3]


def test_005(list1):
    list1.addAtIndex(0, 0)
    assert len(list1) == 4
    assert list1.toArray() == [0, 1, 2, 3]

    list1.addAtIndex(len(list1), 4)
    assert len(list1) == 5
    assert list1.toArray() == [0, 1, 2, 3, 4]

    list1.addAtIndex(1, 10)
    assert len(list1) == 6
    assert list1.toArray() == [0, 10, 1, 2, 3, 4]


def test_006(list1):
    list1.deleteAtIndex(0)
    assert len(list1) == 2
    assert list1.toArray() == [2, 3]


def test_007(list1):
    list1.deleteAtIndex(1)
    assert len(list1) == 2
    assert list1.toArray() == [1, 3]


def test_008(list1):
    list1.deleteAtIndex(2)
    assert len(list1) == 2
    assert list1.toArray() == [1, 2]


def test_009(list1):
    list1.deleteAtIndex(3)
    assert len(list1) == 3
    assert list1.toArray() == [1, 2, 3]


def test_example_1():
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
    assert myLinkedList.get(1) == 2  # return 2
    myLinkedList.deleteAtIndex(1)  # now the linked list is 1->3
    assert myLinkedList.get(1) == 3  # return 3
