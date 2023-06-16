from functools import lru_cache
from typing import List


@lru_cache(None)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        # prepare dp array
        memo = [-1] * (days[-1] + 1)
        durations = [1, 7, 30]

        def dp(n: int):
            if n <= 0:
                return 0

            if memo[n] != -1:
                return memo[n]

            if n in days:
                t = min(dp(n - d) + c
                        for d, c in zip(durations, costs))
            else:
                t = dp(n - 1)

            memo[n] = t
            print(memo)
            return memo[n]

        return dp(days[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
