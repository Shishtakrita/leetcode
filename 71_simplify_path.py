class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part in ('', '.'):
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)




s = Solution()
# print(s.simplifyPath(path="/home/"))
# print(s.simplifyPath(path="/../"))
# print(s.simplifyPath(path="//home//foo/"))
print(s.simplifyPath(path="/../"))

