class Solution(object):
    st = {0: 0, 1: 1}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in self.st:
            return self.st[n]

        fib_sum = self.fib(n - 2) + self.fib(n - 1)
        self.st[n] = fib_sum
        return fib_sum


if __name__ == '__main__':
    # print(Solution().fib(3))
    # print(Solution().fib(4))
    # print(Solution().fib(5))
    print(Solution().fib(7))
