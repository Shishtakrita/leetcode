# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        return self._reverse_list(head)

    def _reverse_list(self, node, prev=None):
        if node is None:
            return prev

        cur = node
        node = node.next
        cur.next = prev
        return self._reverse_list(node, cur)




