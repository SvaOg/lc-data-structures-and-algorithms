from socket import SO_RCVLOWAT


class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_middle(head):
    if not head:
        return None

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def test_get_middle_1():
    head = LinkedNode(1)
    head.next = LinkedNode(2)
    head.next.next = LinkedNode(3)
    head.next.next.next = LinkedNode(4)
    head.next.next.next.next = LinkedNode(5)

    node = get_middle(head)

    assert node.val == 3
