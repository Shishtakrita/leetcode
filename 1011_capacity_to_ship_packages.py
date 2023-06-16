# A conveyor belt has packages that must be shipped from one port to another within days days.
# # The ith package on the conveyor belt has a weight of weights[i].
# Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # find max weight of the list
        lo, hi = max(weights), sum(weights)

        # do binary search starting from lo to hi
        while lo < hi:
            mid = (hi + lo) // 2
            count_weights, count_days = 0, 1

            for w in weights:
                if count_weights + w > mid:
                    count_days += 1
                    count_weights = 0
                count_weights += w

                if count_days > days:
                    break

            if count_days > days:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def shipWithinDays2(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) / 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    # print(s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    # print(s.shipWithinDays([3, 2, 2, 4, 1, 4], 3))

    print(s.shipWithinDays([10, 50, 100, 100, 50, 100, 100, 100], 5))
    # print(s.shipWithinDays2([10, 50, 100, 100, 50, 100, 100, 100], 5))
