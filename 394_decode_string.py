from collections import deque


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = deque()
        prev_char = None
        for char in s:
            if prev_char:
                if (prev_char.isdigit() and char.isdigit()) or (prev_char.isalpha() and char.isalpha()):
                    stack.pop()
                    char = prev_char + char
            if char == ']':
                char = ''
                _pop = stack.pop()
                while not _pop.isdigit():
                    if _pop != '[':
                        char = _pop + char
                    _pop = stack.pop()
                char = int(_pop) * char
            stack.append(char)
            prev_char = char

        res = ''
        while stack:
            res += stack.popleft()

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.decodeString('5[abc]2[xy]'))
    print(s.decodeString('3[a2[c]]'))
    print(s.decodeString('3[a]2[bc]'))
    print(s.decodeString('3[z]2[2[y]pq4[2[jk]e1[f]]]ef'))


# 3[a]2[bc]
# 3[a2[c]]
