class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        chars = {}

        for i in s:
            if i in chars:
                chars.pop(i)
                count += 1
            else:
                chars[i] = 1

        return (count*2) + 1 if chars else count*2

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('abccccdd'))
    print(s.longestPalindrome('ccc'))

