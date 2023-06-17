from typing import List


class UnionFind:
    def __init__(self):
        self.id = {}
        self.size = {}

    def merge(self, p, q):
        px = self.__root(p)
        qx = self.__root(q)

        self.size[px] = px if px in self.size else 1
        self.size[qx] = qx if qx in self.size else 1

        if px != qx:
            if self.size[px] < self.size[qx]:
                self.id[px] = qx
                self.size[qx] += self.size[px]

            else:
                self.id[qx] = px
                self.size[px] += self.size[qx]

    def is_connected(self, p, q):
        if self.__root(p) == self.__root(q):
            return True
        return False

    def __root(self, x):
        if x not in self.id:
            self.id[x] = x
            return x

        while x != self.id[x]:
            self.id[x] = self.id[self.id[x]]
            x = self.id[x]
        return x


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        ignored = []
        for edge in edges:
            if uf.is_connected(edge[0], edge[1]):
                ignored.append(edge)
            else:
                uf.merge(edge[0], edge[1])

        return ignored[-1]


s = Solution()
print(s.findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]]))
print(s.findRedundantConnection(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
