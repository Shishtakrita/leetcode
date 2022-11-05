class Solution(object):

    """
     Dynamic Programming Basics:
     1. Write the Objective Function
        f(i) = minimum cost to climb the ith step
     2. Identify Base Cases
        f(1) - cost[Step 1] - Climb 1 step
        f(2) - Minimum(cost[Step 1] + cost[Step 2], cost[Step 2]) - climb 1 step at a time or climb 2 steps at a time
        f(3) - Minimum(Min cost till step 2 + cost(step 3), Min cost till Step 1 + cost(step 3))
     3. Identify Recurrence relations
        f(n) - Minimum(f[n-1] + cost[step n], f(n-2) + cost[step n])
        f(n) = cost[step n] + min(f(n-1), f(n-2))
     4. Determine Order of Execution
        Come back to this
     5. Where is the answer located
        f(n)
    """

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        first = cost[0]
        second = cost[1]
        if len(cost) <= 2:
            return min(first, second)
        for i in range(2, len(cost)):
            cur_cost = cost[i] + min(first, second)
            first = second
            second = cur_cost

        return min(first, second)














if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([10, 15, 20]))
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
