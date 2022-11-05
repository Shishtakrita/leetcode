from build_bst import BST


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def make_tree_from_level(arr):
    if not arr:
        return None
    root = Node(arr[0])
    q = [root]
    i = 1
    while q:
        next_level = []
        for node in q:
            if node:
                if i < len(arr):
                    node.left = Node(arr[i]) if arr[i] else None
                    next_level.append(node.left)
                    i += 1
                if i < len(arr):
                    node.right = Node(arr[i]) if arr[i] else None
                    next_level.append(node.right)
                    i += 1
        q = next_level
    return root


if __name__ == '__main__':
    tree_key_vals = [1, None, 2, 3]
    bt = make_tree_from_level(tree_key_vals)
    bst = BST(root=bt)
    print(bst.levelorder_traversal())



