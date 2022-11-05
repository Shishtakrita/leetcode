from collections import deque
from build_bst import BST


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        levelAverages = []

        dq = deque()
        dq.append(root)
        while dq:
            _len = len(dq)
            levelSum = 0.0
            for _ in range(_len):
                node = dq.popleft()
                levelSum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            levelAverages.append(levelSum / _len)

        return levelAverages


if __name__ == '__main__':
    tree_key_vals = [3, 9, 20, None, None, 15, 7]
    bst = BST(tree_key_vals)
    print(bst.inorder_traversal())

    s = Solution()
    print(s.averageOfLevels(bst.root))
