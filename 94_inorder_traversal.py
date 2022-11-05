# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def _inorderTraversal(node):
            if node:
                _inorderTraversal(node.left)
                solution.append(node.val)
                _inorderTraversal(node.right)
            return solution

        solution = []
        solution = _inorderTraversal(root)
        return solution




if __name__ == '__main__':
    s = Solution()


