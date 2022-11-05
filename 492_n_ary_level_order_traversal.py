from collections import deque
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if root is None:
            return []

        solution = []
        dq = deque([root])
        while dq:
            _len = len(dq)
            _list = []
            for _ in range(_len):
                node = dq.popleft()
                if node:
                    for child in node.children:
                        dq.append(child)
                    _list.append(node.val)
            solution.append(_list)

        return solution


if __name__ == '__main__':
    s = Solution()









