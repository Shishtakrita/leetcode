from collections import deque


class Solution:
    def levelOrder(self, root):
        queue = deque([root] if root else [])
        ans = []
        while len(queue):
            qlen = len(queue)
            row = []
            for _ in range(qlen):
                curr = queue.popleft()
                row.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            ans.append(row)
        return ans
