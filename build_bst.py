from collections import deque


class Node:
    # constructor
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    root = None

    # build BST with optional default root
    def __init__(self, keys=None, root=None):
        if keys is not None:
            for v in keys:
                if v is not None:
                    self.insert(v)
        else:
            self.root = root

    def get_root(self):
        return self.root

    # insert key into bst
    def insert(self, key):
        self.root = self.__insert(self.root, key)

    # recursive insert keys in binary tree
    def __insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.val:
            node.left = self.__insert(node.left, key)
        elif key > node.val:
            node.right = self.__insert(node.right, key)

        return node

    def inorder_traversal(self):
        def _inorder(node, _list):
            if node:
                _inorder(node.left, _list)
                _list.append(node.val)
                _inorder(node.right, _list)
            return _list

        _list = _inorder(self.root, [])
        return _list

    def preorder_traversal(self):
        def _preorder(node, _list):
            if node:
                _list.append(node.val)
                _preorder(node.left, _list)
                _preorder(node.right, _list)
            return _list

        _list = _preorder(self.root, [])
        return _list

    def postorder_traversal(self):
        def _postorder(node, _list):
            if node:
                _postorder(node.left, _list)
                _postorder(node.right, _list)
                _list.append(node.val)
            return _list

        _list = _postorder(self.root, [])
        return _list

    def levelorder_traversal(self):
        _list = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                _list.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return _list

    def make_tree_from_level(self, arr):
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
                        node.left = Node(arr[i])  # if arr[i] else None
                        next_level.append(node.left)
                        i += 1
                    if i < len(arr):
                        node.right = Node(arr[i])   # if arr[i] else None
                        next_level.append(node.right)
                        i += 1
            q = next_level
        self.root = root


if __name__ == '__main__':
    tree_key_vals = [15, 10, 20, 8, 12, 16, 25]
    bst = BST(keys=tree_key_vals)
    bst.make_tree_from_level([3, 9, 20, None, None, 15, 7])
    print('tree input', tree_key_vals)
    print('preorder traversal', bst.preorder_traversal())
    print('postorder traversal', bst.postorder_traversal())
    print('inorder traversal:', bst.inorder_traversal())
    print('levelorder traversal:', bst.levelorder_traversal())
