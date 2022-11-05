from build_bst import BST


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def _verticalTraversal(node, verticalNum, horizontalNum):
            if node.left:
                _verticalTraversal(node.left, verticalNum - 1, horizontalNum + 1)
            if verticalNum in hmap:
                hmap[verticalNum].append([horizontalNum, node.val])
            else:
                hmap[verticalNum] = [[horizontalNum, node.val]]
            if node.right:
                _verticalTraversal(node.right, verticalNum + 1, horizontalNum + 1)

        solution, hmap = [], {}
        _verticalTraversal(root, 0, 0)
        for key in sorted(hmap):
            arr = sorted(hmap[key])
            solution.append([arr[i][1] for i in range(len(arr))])
        return solution


if __name__ == '__main__':
    tree_key_vals = [0, 10, 1, None, None, 2, 4, 3, 5, None, None, 6, None, 7, 9, 8, None, None, None, None, 11, None,
                     None, 12]
    bst = BST(keys=tree_key_vals)
    bst.make_tree_from_level(tree_key_vals)
    print(bst.levelorder_traversal())
    s = Solution()
    print(s.verticalTraversal(bst.root))
