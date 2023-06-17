from typing import List


class UnionFind:
    def __init__(self, n):
        self.id = [-1] * n
        self.size = [1] * n
        for i in range(len(self.id)):
            self.id[i] = i

    def union(self, p, q):
        px = self.__root(p)
        qx = self.__root(q)
        if px != qx:
            if self.size[px] < self.size[qx]:
                self.id[px] = qx
                self.size[qx] += self.size[px]
            else:
                self.id[qx] = px
                self.size[px] += self.size[qx]

    def is_connected(self, p, q):
        return self.__root(p) == self.__root(q)

    def __root(self, x):
        print('x is: ', x)
        print(self.id)
        while x != self.id[x]:
            self.id[x] = self.id[self.id[x]]
            x = self.id[x]
        return x


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lrow = len(board)
        lcol = len(board[0])
        uf = UnionFind((lrow * lcol) + 1)

        for i in range(lrow):
            for j in range(lcol):
                if (i == 0 or j == 0 or i == lrow - 1 or j == lcol - 1) and board[i][j] == 'O':
                    # connect to sentient node
                    uf.union(i * lrow + j, lrow * lcol)
                else:
                    # connect O to surrounding O
                    if board[i][j] == 'O':
                        print(i, lrow, j)
                        if i > 0 and board[i - 1][j] == 'O':
                            uf.union(i * lrow + j, (i - 1) * lrow + j)
                        if i < lrow - 1 and board[i + 1][j] == 'O':
                            uf.union(i * lrow + j, (i + 1) * lrow + j)
                        if j < lcol - 1 and board[i][j + 1] == 'O':
                            uf.union(i * lrow + j, i * lrow + (j + 1))
                        if j > 0 and board[i][j - 1] == 'O':
                            uf.union(i * lrow + j, i * lrow + (j - 1))

        for i in range(lrow):
            for j in range(lcol):
                if board[i][j] == 'O':
                    if not uf.is_connected(i * lrow + j, lrow * lcol):
                        board[i][j] = 'X'


s = Solution()
s.solve(
    board=[["X", "O", "X", "X"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"],
           ["O", "X", "O", "X"]])
