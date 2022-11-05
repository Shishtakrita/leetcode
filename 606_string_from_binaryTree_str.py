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
        def _preOrderTraversal(node, _text):

            if node is None:
                _text += '()'
                return None, _text

            _text += '(' + str(node.val)
            if node.left or node.right:
                node.left, _text = _preOrderTraversal(node.left, _text)
            if node.right:
                node.right, _text = _preOrderTraversal(node.right, _text)
            _text += ')'

            return node, _text

        _text = ''
        root, _text = _preOrderTraversal(root, _text)
        return _text


if __name__ == '__main__':
    s = Solution()
    root = [1, 2, 3, 4]
    # root = [1, 2, 3, None, 4]
    bst = BST()
    bst.make_tree_from_level(root)
    print(bst.levelorder_traversal())
    print('text:', s.tree2str(bst.root))

