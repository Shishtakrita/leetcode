class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l = len(prices)
        if l < 2:
            return 0

        sum = 0
        min_ = prices[0]
        for i in range(1, l):
            min_ = min(min_, prices[i])
            sum = max(sum, prices[i]-min_)

        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 6, 4, 3, 1]))
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([1, 2, 4]))
    print(s.maxProfit([2, 1, 2, 0, 1]))

