class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                return
            if grid[i][j] == '0':
                return
            if grid[i][j] == '1':
                grid[i][j] = '#'
                dfs(grid, i + 1, j)
                dfs(grid, i - 1, j)
                dfs(grid, i, j + 1)
                dfs(grid, i, j - 1)

        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    s = Solution()
    print(s.numIslands(grid))
