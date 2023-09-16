from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def recurse(curr, size):
            if size > k:
                results.append(curr[:])
                return

            for i in range(1, n + 1):
                if i not in hash_set:
                    hash_set.add(i)
                    curr.append(i)
                    recurse(curr, size + 1)
                    hash_set.remove(i)
                    curr.pop()

        results = []
        hash_set = set()
        recurse([], 0)

        return results


s = Solution()
print(s.combine(n=5, k=2))
