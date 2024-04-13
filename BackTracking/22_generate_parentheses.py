from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def helper(opRemaining: int, clRemaining: int, soFar: str):
            # print('opRemaining:{0}, clRemaining: {1}, soFar:{2}'.format(opRemaining, clRemaining, soFar))
            if opRemaining == clRemaining == 0:
                results.append(soFar)
            elif opRemaining > clRemaining:
                return
            elif opRemaining < 0 or clRemaining < 0:
                return
            else:
                helper(opRemaining - 1, clRemaining, soFar + '(')
                helper(opRemaining, clRemaining - 1, soFar + ')')
            return results

        results = helper(n, n, '')
        return results


s = Solution()
print(s.generateParenthesis(3))
