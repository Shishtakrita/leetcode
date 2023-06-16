from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dp(n):
            if n < 0:
                return 0
            if n == 0:
                memo[n] = nums[0]
            if n in memo:
                return memo[n]
            memo[n] = max(nums[n] + dp(n - 2), nums[n - 1] + dp(n - 3))
            return memo[n]

        return dp(len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.rob(nums=[2,7,9,3,1]))
