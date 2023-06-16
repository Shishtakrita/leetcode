from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = [[0] * len(grid[0]) for i in range(len(grid))]

        if grid[0][0] != 0:
            return -1

        def dp(row, col, steps):

            # if goes out of boundary,
            if row < 0 or row > len(grid)-1:
                return steps
            if col < 0 or col > len(grid[0])-1:
                return steps
            # if destination is reached, return
            if row == len(grid) and col == len(grid[0]) and grid[row][col] == 0:
                visited[row][col] = steps
                return steps
            # if no valid path found, return
            if grid[row][col] == -1:
                return steps
            # if already visited, return
            if visited[row][col] != 0:
                return steps
                # go in all 8 directions, find out min steps
            a = dp(row, col + 1, steps)  # right
            b = dp(row, col - 1, steps)  # left
            c = dp(row + 1, col, steps)  # down
            d = dp(row - 1, col, steps)  # up
            e = dp(row + 1, col + 1, steps)  # down right diag
            f = dp(row + 1, col - 1, steps)  # down left diag
            g = dp(row - 1, col + 1, steps)  # top right diag
            h = dp(row - 1, col - 1, steps)  # top left diag
            best = min(a, b, c, d, e, f, g, h)
            if best <= 0:
                visited[row][col] = -1
                return 0
            else:
                visited[row][col] = best + 1
                return best + 1

        ans = dp(0, 0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.shortestPathBinaryMatrix(grid=[[0, 0, 0, 2], [1, 1, 0, 4], [1, 1, 0, 9]])
