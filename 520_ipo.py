from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = sorted(list(zip(capital, profits)))
        c = 0
        pq = []
        for i in range(k):
            if i > len(profits) - 1:
                break

            while c < len(profits) and projects[c][0] <= w:
                heapq.heappush(pq, -projects[c][1])
                c += 1

            if not pq:
                break
            w += -heapq.heappop(pq)

        return w


if __name__ == '__main__':
    s = Solution()
    # print(s.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
    # print(s.findMaximizedCapital(k = 3, w = 0, profits = [1, 2, 3], capital = [0, 1, 2]))
    print(s.findMaximizedCapital(k=1, w=2, profits=[1, 2, 3], capital=[1, 1, 2]))
