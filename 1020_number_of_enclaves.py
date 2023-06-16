from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if grid[i][j] == 0:
                return
            if grid[i][j] == 2:
                return
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                return
            if grid[i][j] == 1:
                grid[i][j] = 2  # visited

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        # dfs from all boundaries
        for j in range(len(grid[0])):
            dfs(0, j)

        for j in range(len(grid[0])):
            dfs(len(grid) - 1, j)

        for i in range(len(grid)):
            dfs(i, 0)

        for i in range(len(grid)):
            dfs(i, len(grid[0]) - 1)

        # count all remaining 1's
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1

        return count


s = Solution()
print(s.numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(s.numEnclaves(grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
