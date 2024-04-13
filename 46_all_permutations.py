# backtracking
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(soFar: List[int], available: List[int]):
            if not available:
                results.append(soFar[:])  # deep copy
            else:
                for i in range(len(available)):
                    chosen = available.pop(i)
                    soFar.append(chosen)
                    helper(soFar, available)
                    soFar.pop()
                    available.insert(i, chosen)
            return results

        results = []
        return helper([], nums)


s = Solution()
print(s.permute(nums=[1, 1, 2]))
