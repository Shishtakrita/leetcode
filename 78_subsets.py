from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(soFar: List[int],  start: int):
            results.append(soFar[:])
            print('soFar={0}, start={1}, {2}'.format(soFar, start, results))
            for i in range(start, len(nums)):
                chosen = nums.pop(i)
                soFar.append(chosen)
                helper(soFar, i)
                soFar.pop()
                nums.insert(i, chosen)
            return results

        results = []
        return helper([], 0)


s = Solution()
print(s.subsets(nums=[1, 2, 2]))
