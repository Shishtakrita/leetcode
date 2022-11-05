class Solution:
    def oneSidedBinarySearch(self, nums, target):
        i = 1
        while i <= len(nums) - 1:
            if nums[i] == target:
                break
            else:
                i = i * 2
        return self._oneSidedBinarySearch(nums[:i], target, 0, i)

    def _oneSidedBinarySearch(self, n, target, low, high):
        if low > high:
            return low
        middle = low + (high - low) // 2
        if n[middle] < target:
            return self._oneSidedBinarySearch(n, target, middle+1, high)
        else:
            return self._oneSidedBinarySearch(n, target, low, middle-1)


if __name__ == '__main__':
    s = Solution()
    n = ([0] * 100) + ([1]*300)
    print(s.oneSidedBinarySearch(n, 1))
