# Definition for a binary tree node.
import sys

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        prev = TreeNode(-sys.maxsize)
        return self._isValidBST(root, prev)

    def _isValidBST(self, node, prev):
        if node is None:
            return True

        left = self._isValidBST(node.left, prev)
        if node.val <= prev.val:
            return False
        prev.val = node.val
        right = self._isValidBST(node.right, prev)
        return left and right

# replacing the node value with int parameter did not work, please investigate