class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)

    def removeStars_2ptr(self, s: str) -> str:

        hi = 0
        ans = [''] * len(s)

        for c in s:
            if c == '*':
                hi -= 1
            else:
                ans[hi] = c
                hi += 1

        return ''.join(ans[:hi])




s = Solution()
print(s.removeStars(s="leet**cod*e"))
print(s.removeStars_2ptr(s="leet**cod*e"))
