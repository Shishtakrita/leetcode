class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # i, j = 0, len(s) - 1

        memo = {}

        def lps(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i > j:
                return 0

            if s[i] == s[j]:
                ans = 2 + lps(i + 1, j - 1)
            else:
                ans = max(lps(i, j - 1), lps(i + 1, j))

            memo[(i, j)] = ans
            return ans

        return lps(0, len(s) - 1)

    def longestPalindromeSubseq_iterative(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


s = Solution()
print(s.longestPalindromeSubseq_iterative(s="bbbab"))
