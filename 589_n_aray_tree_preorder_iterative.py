"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        s = deque()
        s.append(root)
        trace = []
        while s:
            node = s.pop()
            if node:
                trace.append(node.val)
                temp = []
                for i in node.children:
                    temp.append(i)
                for i in range(0, len(temp)):
                    s.append(temp.pop())

        return trace

