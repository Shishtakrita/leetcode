# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        last_node_position = 0
        if head.next is None:
            return head

        next = head.next
        next.next = self.removeNode(self, head, n, False)
        return head


        def removeNode(self, node, n, last_node_pos, last_node_found):
            if node.next is None:
                last_node_position =
                return self.removeNode(node, n, 0, True)

            if abs(last_node_pos) == n:
                return node.next

            while not last_node_found:
                node.next = self.removeNode(node.next, n, 1)





