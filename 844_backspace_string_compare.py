class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sStack, tStack = [], []
        for i in range(len(s)):
            if s[i] == '#':
                if sStack:
                    sStack.pop()
            else:
                sStack.append(s[i])

        for i in range(len(t)):
            if t[i] == '#':
                if tStack:
                    tStack.pop()
            else:
                tStack.append(t[i])

        return sStack == tStack


if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare('ab#c', 'ad#c'))
    print(s.backspaceCompare('ab##', 'c#d#'))
    print(s.backspaceCompare('a#c', 'b'))
