# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
1 2 3
1 2 3 4
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        counter = 0
        slow_counter = 0
        slow = head
        if head.next:
            fast = head.next

        while head.next and head.next.next:
            slow = slow.next
            head = head.next.next
            counter += 2
            slow_counter += 1

        if head.next:
            counter += 1

        while slow_counter < counter - 1:
            slow = slow.next







