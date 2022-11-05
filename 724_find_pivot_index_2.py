class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lsum = 0
        rsum = sum(nums)
        for i, v in enumerate(nums):
            rsum -= v
            if lsum == rsum:
                return i
            lsum += v

        return -1


if __name__ == '__main__':
    n = [1,2,3]
    s = Solution()
    print(s.pivotIndex(n))
