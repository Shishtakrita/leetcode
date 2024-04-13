from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(soFar: List[int], available: List[int], sumSoFar: int, start: int):
            if sumSoFar == target:
                results.append(soFar[:])  # deep copy
            elif sumSoFar > target:
                pass
            else:
                for i in range(start, len(available)):
                    chosen = available.pop(i)
                    soFar.append(chosen)
                    helper(soFar, available, sumSoFar + chosen, i)
                    soFar.pop()
                    available.insert(i, chosen)
            return results

        results = []
        return helper(soFar=[], available=candidates, sumSoFar=0, start=0)


s = Solution()
print(s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
