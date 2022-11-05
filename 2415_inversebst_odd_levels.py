from build_bst import BST

# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        level = 0
        solution = []
        dq = deque([root])
        while dq:
            qLen = len(dq)
            s = []
            for _ in range(qLen):
                node = dq.popleft()
                s.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if level % 2 == 1:
                solution.append(s)
            level += 1

        print(solution)


if __name__ == '__main__':
    bst = BST()
    bst.make_tree_from_level([2, 3, 5, 8, 13, 21, 34])
    print(bst.levelorder_traversal())
    s = Solution()
    s.reverseOddLevels(bst.root)


