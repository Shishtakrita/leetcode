from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (hi - mid + 1) % 2:
                if nums[mid] == nums[mid - 1]:
                    hi = mid
                elif nums[mid] == nums[mid + 1]:
                    lo = mid
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    lo = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    hi = mid - 1

        return nums[lo]


if __name__ == '__main__':
    s = Solution()
    print(s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
