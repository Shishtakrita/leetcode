"""
write notes to understand why this greedy approach will not work.
the below problem is a wrong solution

"""

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        left, right = 0, len(nums) - 1
        max_iter = len(multipliers) - 1
        sum = 0

        def _maximumScore(left, right, i, sum):

            if i > max_iter:
                return sum

            if nums[left] * multipliers[i] > nums[right] * multipliers[i]:
                sum += nums[left] * multipliers[i]
                left += 1
            else:
                sum += nums[right] * multipliers[i]
                right -= 1

            return _maximumScore(left, right, i + 1, sum)

        return _maximumScore(left, right, 0, sum)


if __name__ == '__main__':
    s = Solution()
    # print(s.maximumScore(nums=[1, 2, 3], multipliers=[3, 2, 1]))
    print(s.maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]))
