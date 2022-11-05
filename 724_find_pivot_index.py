class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lsum = rsum = 0
        for num in nums:
            rsum += num

        i = 0
        l = len(nums)
        rsum -= nums[i]
        while lsum != rsum:
            if i == l - 1:
                return -1

            lsum += nums[i]
            i += 1
            if i == l - 1:
                rsum = 0
            else:
                rsum -= nums[i]

        return i


if __name__ == '__main__':
    n = [-1, 1, 2]
    s = Solution()
    print(s.pivotIndex(n))
