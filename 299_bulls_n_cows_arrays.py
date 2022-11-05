class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        a = [0] * 10
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            if s == g:
                bulls += 1
            else:
                if a[g] > 0:
                    cows += 1
                if a[s] < 0:
                    cows += 1
                a[s] += 1
                a[g] -= 1

        return '{0}A{1}B'.format(bulls, cows)


if __name__ == '__main__':
    s = Solution()
    print(s.getHint("1123", "0111"))
    print(s.getHint("1807", "7810"))
    print(s.getHint("2962", "7236"))
