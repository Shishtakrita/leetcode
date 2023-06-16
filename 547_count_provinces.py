from typing import List


class Solution:
    class UnionFind:

        def __init__(self, k):
            self.len = k
            self.size = [0] * k
            self.connected_count = k

            # index in id array has the index of the element's root
            self.id = []
            for i in range(k):
                self.id.append(i)

        def connected(self, p, q):
            return self.root(p) == self.root(q)

        def merge(self, p, q):

            # find the size of each tree and make the smaller tree a child of the larger tree
            px = self.root(p)
            qx = self.root(q)

            if px == qx:
                return

            if self.size[px] < self.size[qx]:
                self.id[px] = qx
                self.size[qx] += self.size[px]
            else:
                self.id[qx] = px
                self.size[px] += self.size[qx]
            self.connected_count -= 1

        # def root(self, i):
        #
        #     # 2 pass variant
        #     # find the root first
        #     x = i
        #     while i != self.id[i]:
        #         i = self.id[i]
        #     # variable i is now the root
        #
        #     # reset the root value in all nodes
        #     while x != i:
        #         # get the root value
        #         parent = self.id[x]
        #         self.id[x] = i
        #         x = parent

        def root(self, i):
            if i == self.id[i]:
                return i
            self.id[i] = self.root(self.id[i])
            return self.id[i]

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = self.UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    uf.merge(i, j)

        return uf.connected_count


if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(s.findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
