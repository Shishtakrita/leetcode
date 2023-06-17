from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_streak = 1
        num_set = set(nums)

        if not nums:
            return 0

        for i in num_set:
            if i - 1 not in num_set:
                current = i
                current_streak = 1

                while current + 1 in num_set:
                    current += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


s = Solution()

print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(s.longestConsecutive(nums = [100,4,200,1,3,2]))
