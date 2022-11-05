class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        st = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0

        for i in range(0, len(s)):
            if i + 1 < len(s) and st[s[i]] < st[s[i+1]]:
                num -= st[s[i]]
            else:
                num += st[s[i]]

        return num


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MMMCDXC'))
    # print(s.romanToInt('MCMXCIV'))







