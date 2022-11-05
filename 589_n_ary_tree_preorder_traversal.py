"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self._preorder(root, [])

    def _preorder(self, node, trace):

        if not node:
            return trace
        trace.append(node.val)
        for i in node.children:
            trace = self._preorder(i, trace)
        return trace



