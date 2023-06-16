from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                return False
            if grid[i][j] == 1 or grid[i][j] == 2:
                return True

            grid[i][j] = 2
            b = dfs(i + 1, j)
            b = b & dfs(i - 1, j)
            b = b & dfs(i, j - 1)
            b = b & dfs(i, j + 1)
            return b

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and dfs(i, j):
                    count += 1

        return count


s = Solution()
print(s.closedIsland(
    grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 0]]))
