from build_bst import BST, Node


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
        return node



if __name__ == '__main__':
    keys = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    bst = BST(keys)
    print("level order traversal:", bst.levelorder_traversal())
    s = Solution().lowestCommonAncestor(bst.get_root(), Node(5), Node(0))
    print('ancestor=', s.val)

