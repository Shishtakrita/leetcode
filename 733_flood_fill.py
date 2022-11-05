class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(image) - 1 or j > len(image[0]) - 1:
                return
            if image[i][j] != pixel_val or image[i][j] == color:
                return
            else:
                image[i][j] = color
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        # do dfs
        pixel_val = image[sr][sc]
        dfs(sr, sc)

        return image


if __name__ == '__main__':
    s = Solution()
    # print(s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
    print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
