from collections import Counter
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def helper(soFar: List[int], freq: int):
            print('soFar={0}, freq={1}'.format(soFar, freq))
            results.append(soFar[:])
            if freq < 1:
                pass
            else:
                for i in range(len(counter)):
                    num, freq = counter[i]
                    counter[i] = (num, freq - 1)
                    soFar.append(num)
                    helper(soFar, freq - 1)
                    soFar.pop()
                    counter[i] = (num, freq)
                return results

        results = []
        counter = Counter(nums)
        counter = [(k, counter[k]) for k in counter.keys()]
        return helper([], 1)

s = Solution()
print(s.subsetsWithDup(nums=[1, 2, 2]))
