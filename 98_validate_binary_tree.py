# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isValidBST(root, float('-inf'), float('inf'))

    def _isValidBST(self, node, floor, ceiling):
        if not node:
            return True
        if node.val <= floor or node.val >= ceiling:
            return False

        return self._isValidBST(node.left, floor, node.val) and \
               self._isValidBST(node.right, node.val, ceiling)

# [120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]
