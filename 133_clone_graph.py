# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Node) -> Node:

        def dfs(n: Node) -> Node:
            # mark node as visited
            if n.val in self.visited:
                return self.visited[n.val]

            # create a new node
            clone = Node(n.val)
            # mark as visited
            self.visited[n.val] = clone
            for neighbor in n.neighbors:
                t = dfs(neighbor)
                clone.neighbors.append(t)

            return clone

        return None if node is None else dfs(node)

