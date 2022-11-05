class Solution(object):

    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        def _numSameConsecDiff(num, CurrLen):
            if len(num) == n:
                solution.append(num)
                return

            lastDigit = num[-1]
            negate = int(lastDigit) - k
            add = int(lastDigit) + k
            if 0 <= negate <= 9:
                _numSameConsecDiff(num + str(negate), CurrLen + 1)
            if k != 0:  # avoid repeat of same numbers if k = 0
                if 0 <= add <= 9:
                    _numSameConsecDiff(num + str(add), CurrLen + 1)

        solution = []
        for i in range(1, 10):
            _numSameConsecDiff(str(i), 1)
        return solution


if __name__ == '__main__':
    s = Solution()
    print(s.numsSameConsecDiff(3, 7))
    print(s.numsSameConsecDiff(2, 1))
    print(s.numsSameConsecDiff(2, 0))
