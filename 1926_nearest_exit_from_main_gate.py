from typing import List


class Solution:
    class WeightedQuickUnion:
        def __init__(self, maze: List[List[str]], entrance: List[int]):
            self.row_size = len(maze)
            self.col_size = len(maze[0])
            self.id = list(range(0, self.row_size * self.col_size))
            self.sz = [0] * self.row_size * self.col_size

        def connected(self, p, q):
            return self.root(p) == self.root(q)

        def union(self, p, q):
            i = self.root(p)
            j = self.root(q)
            if i == j:
                return
            if self.sz[i] < self.sz[j]:
                self.id[i] = j
                self.sz[j] += self.sz[i]
            else:
                self.id[j] = i
                self.sz[i] += self.sz[j]

        def root(self, i):
            while i != self.id[i]:
                self.id[i] = self.id[self.id[i]]
                i = self.id[i]
            return i


    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        wuf = self.WeightedQuickUnion(maze, entrance)
        for r in range(len(maze)):
            for c in range  (len(maze[0])):
                if maze[r][c] == '.':
                    if r == entrance[0] and c == entrance[1]:
                        continue
                    else:
                        #down
                        if r+1 <= len(maze) and maze[r+1][c] == '.':
                        #up
                        if r-1 >= 0 and maze[r-1][c] == '.':
                        #left
                        if c-1 >= 0 and maze[r][c-1] == '.':
                        # right
                        if c+1 <= len(maze[0]) and maze[r][c+1] == '.':




