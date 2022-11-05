from build_bst import BST

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preOrderTraversal(node):

            if node is None:
                s.append('()')
                return None

            s.append('(' + str(node.val))
            if node.left or node.right:
                node.left = preOrderTraversal(node.left)
            if node.right:
                node.right = preOrderTraversal(node.right)
            s.append(')')

            return node

        s = []
        root = preOrderTraversal(root)
        return ''.join(s)[1:-1]


if __name__ == '__main__':
    s = Solution()
    root = [1, 2, 3, 4]
    # root = [1, 2, 3, None, 4]
    bst = BST()
    bst.make_tree_from_level(root)
    print(bst.levelorder_traversal())
    print('text:', s.tree2str(bst.root))
