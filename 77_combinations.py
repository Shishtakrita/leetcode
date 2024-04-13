from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def helper(soFar: List[int], currNum: int, soFarCount: int):
            print('soFar={0}, currNum={1}, soFarCount={2},{3}'.format(soFar, currNum, soFarCount, results))
            if soFarCount == k:
                results.append(soFar[:])
            elif currNum > n:
                pass
            else:
                for i in range(currNum, n + 1):
                    soFar.append(i)
                    helper(soFar, i + 1, soFarCount + 1)
                    soFar.pop()
                return results

        results = []
        return helper([], 1, 0)


s = Solution()
print(s.combine(n=4, k=2))
