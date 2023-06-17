from typing import List


class Solution:
    # Recursion + Storage(Memoization)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = [-1 for _ in range(days[-1] + 1)]
        return self.minCostTicketsHelper(days, costs, days[-1], memo)

    def minCostTicketsHelper(self, days, costs, n, memo):
        if n <= 0:
            return 0
        if memo[n] != -1:
            return memo[n]

        memo[n] = min(
            self.minCostTicketsHelper(days, costs, n - 1, memo) + costs[0] if n in days else
            self.minCostTicketsHelper(days, costs, n - 1, memo) + 0,
            # Cost till previous day + today's cost, here If condition is to exclude current day's cost if not travelling today
            self.minCostTicketsHelper(days, costs, n - 7, memo) + costs[1],  # Cost till 7 days back + 7 day pass cost
            self.minCostTicketsHelper(days, costs, n - 30, memo) + costs[2]  # Cost till 30 days back + 30 day pass cost
        )
        return memo[n]

if __name__ == '__main__':
    s = Solution()
    print(s.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))


