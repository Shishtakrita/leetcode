from typing import List


class Solution():
    def search_left(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < k:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def search_right(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > k:
                hi = mid - 1
            else:
                lo = mid

        return lo


s = Solution()
a = s.search_left(nums=[1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3], k=2)
b = s.search_right(nums=[1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3], k=2)
print(b - a + 1)
