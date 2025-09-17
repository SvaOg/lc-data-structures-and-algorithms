from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


# Helper functions for testing
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
