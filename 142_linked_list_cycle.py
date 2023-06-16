from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        bag = set()

        if not head.next:
            return None

        while head.next:
            head = head.next
            if head in bag:
                return head

            bag.add(head)

        return None



