from typing import List


class UnionFind:
    def __init__(self, nums):
        self.id = {}
        self.size = {}
        self.max_size = 1 if nums else 0

        for i in nums:
            self.id[i] = i
            self.size[i] = 1

    def merge(self, p, q):
        px = self.__root(p)
        qx = self.__root(q)

        if px != qx:
            if self.size[px] < self.size[qx]:
                self.id[px] = qx
                self.size[qx] += self.size[px]
            else:
                self.id[qx] = px
                self.size[px] += self.size[qx]
            self.max_size = max(self.max_size, self.size[px], self.size[qx])

    def is_connected(self, p, q):
        if self.__root(p) == self.__root(q):
            return True
        return False

    def __root(self, p):
        orig = p
        while p != self.id[p]:
            p = self.id[p]

        root = p
        p = orig

        while self.id[p] != root:
            parent = self.id[p]
            self.id[p] = root
            p = parent

        return root


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)
        seen = {}
        for i in nums:
            seen[i] = i
            if i - 1 in seen:
                uf.merge(i, i - 1)
            if i + 1 in seen:
                uf.merge(i, i + 1)
        return uf.max_size


s = Solution()
print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
