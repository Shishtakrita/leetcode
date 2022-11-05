# Definition for a binary tree node.
from typing import Optional
from build_bst import BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def _pruneTree(node):
            if node is None:
                return None

            node.left = _pruneTree(node.left)
            node.right = _pruneTree(node.right)

            if node.val == 0 and node.left is None and node.right is None:
                return None

            return node

        return _pruneTree(root)


if __name__ == '__main__':
    s = Solution()
    tree_keys = [1, None, 0, 0, 1]
    bst = BST()
    bst.make_tree_from_level(tree_keys)
    bst.root = s.pruneTree(bst.root)
    print(bst.levelorder_traversal())

