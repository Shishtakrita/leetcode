from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        farthest = 0
        from_index = 0
        range_of_index = nums[from_index]
        end = len(nums) - 1

        def jump_helper(from_index, range_of_index):
            if range_of_index >= end:
                return

            for i in range(from_index + 1, range_of_index + 1):
                print










if __name__ == '__main__':
    nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
    s = Solution()
    print(s.jump(nums))
