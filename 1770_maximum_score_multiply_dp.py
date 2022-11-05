"""
write notes to understand why a greedy approach will not work.
below is a recursive dp approach
"""

from typing import List


class Solution:
    # """
    # This is efficient bottom up approach - understand this later
    # """
    #
    # def maximumScore(self, nums: List[int], mul: List[int]) -> int:
    #     dp = [0] * (len(mul) + 1)
    #     for m in range(len(mul) - 1, -1, -1):
    #         pd = [0] * (m + 1)
    #         for l in range(m, -1, -1):
    #             pd[l] = max(dp[l + 1] + mul[m] * nums[l],
    #                         dp[l] + mul[m] * nums[~(m - l)])
    #         dp = pd
    #     return dp[0]

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        max_iter = len(multipliers) - 1
        dp = [[-1 for _ in range(len(multipliers))] for _ in range(len(multipliers))]

        def print_dp(arr):
            s = '[' + '\n'
            for a in arr:
                s += (' ' * 5) + str(a) + '\n'
            s += ']' + '\n'
            print(s)

        def dfs(l, r, i):
            if i > max_iter:
                return 0
            if dp[l][i] != -1:
                return dp[l][i]
            print(l, i)
            left = nums[l] * multipliers[i] + dfs(l + 1, r, i + 1)
            right = nums[r] * multipliers[i] + dfs(l, r - 1, i + 1)
            dp[l][i] = max(left, right)
            # print_dp(dp)
            return dp[l][i]

        return dfs(0, len(nums) - 1, 0)

    def maximumScore_iter(self, nums: List[int], multipliers: List[int]) -> int:
        dp = [[0 for _ in range(len(multipliers) + 1)] for _ in range(len(multipliers) + 1)]
        n = len(nums)
        m = len(multipliers)

        for l in range(m - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if i >= l:
                    r = n - 1 - (i - l)
                    left = nums[l] * multipliers[i] + dp[l + 1][i + 1]
                    right = nums[r] * multipliers[i] + dp[l][i + 1]
                    dp[l][i] = max(left, right)
        return dp[0][0]


    def maximumScore_opt(self, nums: List[int], multipliers: List[int]) -> int:
        dp = [0 for _ in range(len(multipliers) + 1)]
        n = len(nums)
        m = len(multipliers)

        for l in range(m - 1, -1, -1):
            pd = [0 for _ in range(l + 1)]
            for i in range(m - 1, -1, -1):
                if i >= l:
                    r = n - 1 - (i - l)
                    left = nums[l] * multipliers[i] + dp[l + 1][i + 1]
                    right = nums[r] * multipliers[i] + dp[l][i + 1]
                    dp[l][i] = max(left, right)
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    # print(s.maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]))
    print(s.maximumScore_iter(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]))
