# Definition for a binary tree node.
import copy


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def allPossibleFBT(self, n):
        if n <= 0:
            return []
        if n % 2 == 0:
            return []
        if n == 1:
            return TreeNode()

        ans = []
        root = TreeNode()
        leaves = []

        def update_tree(node, leaves, remaining):
            if remaining == 0:
                ans.append(copy.deepcopy(node))

            node.left = TreeNode()
            node.right = TreeNode()
            leaves.append(node.left)
            leaves.append(node.right)
            remaining -= 2
            # used for backtracking??. how?
            size = len(leaves) - 1

            while leaves:
                curr_node = leaves.pop()
                update_tree(curr_node, leaves[:size], remaining)

                # back track
                curr_node.left = curr_node.right = None
                if n == 0:
                    break

        update_tree(root, leaves, n - 1)
        return ans