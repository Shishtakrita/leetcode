class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        def _factorial(num):
            if num <= 0:
                return 1

            res = 1
            while num > 0:
                res = res * num
                num -= 1
            return res

        count_of_2 = n // 2
        count_of_1 = n % 2
        combinations = 0

        while count_of_2 > 0:
            combinations += _factorial(count_of_2 + count_of_1)/(_factorial(count_of_2) * _factorial(count_of_1))
            count_of_2 -= 1
            count_of_1 += 2

        return int(combinations + 1)


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(5))
    print(s.climbStairs(6))
    print(s.climbStairs(7))
    print(s.climbStairs(8))
    print(s.climbStairs(9))






