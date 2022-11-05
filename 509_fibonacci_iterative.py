class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            i = 2
            fib_sum = 0
            while i <= n:
                fib_sum = a + b
                a, b = b, fib_sum
                i += 1

            return fib_sum


if __name__ == '__main__':
    print(Solution().fib(3))
    print(Solution().fib(4))
    print(Solution().fib(5))
    print(Solution().fib(7))





