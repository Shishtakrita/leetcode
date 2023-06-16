from typing import List
import math, heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        max_, min_deviation = -math.inf, math.inf

        pq = []
        for i, n in enumerate(nums):
            o = n
            while n % 2 == 0:
                n = n // 2
            nums[i] = n
            heapq.heappush(pq, [n, o])
            max_ = max(max_, n)

        while True:
            n, o = heapq.heappop(pq)
            min_deviation = min(min_deviation, max_ - n)

            if n % 2 == 1 or n < o:
                max_ = max(max_, n * 2)
                heapq.heappush(pq, [n * 2, o])
            else:
                break

        return min_deviation

if __name__ == '__main__':
    s = Solution()
    # print(s.minimumDeviation([1, 2, 3, 4]))
    print(s.minimumDeviation([4, 1, 5, 20, 3]))
    # print(s.minimumDeviation([2, 10, 8]))
    # print(s.minimumDeviation([3, 5]))
    print(s.minimumDeviation([4, 9, 4, 5]))
    print(s.minimumDeviation([10, 4, 3]))

