# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        node = dummy
        while list1 and list2:
            if list2.val < list1.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists([1,2,4],[1,3,4]))
