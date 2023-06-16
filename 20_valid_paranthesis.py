class Solution:
    def isValid(self, s: str) -> bool:

        '''
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
        '''

        stack = []
        for c in s:
            if c in (')', '}', ']'):
                if len(stack) == 0:
                    return False
                removed = stack.pop()

                if c == ')' and removed != '(': return False
                if c == ']' and removed != '[': return False
                if c == '}' and removed != '{': return False

            elif c in ('(', '{', '['):
                stack.append(c)
            else:
                return False

        return True if len(stack) == 0 else False


s = Solution()
print(s.isValid('()'))
print(s.isValid("()[]{}"))
print(s.isValid("([][])"))
print(s.isValid("([][]}"))
print(s.isValid("(]"))




