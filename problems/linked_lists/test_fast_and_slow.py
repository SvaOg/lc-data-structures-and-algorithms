from typing import Optional
from dataclasses import dataclass


@dataclass
class ListNode[T]:
    val: T
    next: "Optional[ListNode[T]]" = None


def get_middle[T](head: Optional[ListNode[T]]) -> Optional[ListNode[T]]:
    if head is None:
        return None

    slow = head
    fast = head
    while fast and fast.next:
        assert slow is not None
        slow = slow.next
        fast = fast.next.next

    return slow


def test_get_middle_1():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    node = get_middle(head)
    assert node is not None
    assert node.val == 3
