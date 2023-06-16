from typing import List


class Solution:
    def find_num(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > k:
                hi = mid
            else:
                lo = mid + 1

        return lo


s = Solution()
print(s.find_num(nums=[1, 2, 3, 4, 6, 7, 8], k=5))
