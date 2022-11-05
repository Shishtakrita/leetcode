class Solution:
    def countOccurences(self, nums, target):
        right = self.binarySearchRightBoundary(nums, target, 0, len(nums) - 1)
        left = self.binarySearchLeftBoundary(nums, target, 0, right)
        return left, right

    def binarySearchRightBoundary(self, s, key, low, high):
        if low > high:
            return high
        middle = low + (high - low) // 2
        middle_val = s[middle]
        if s[middle] > key:
            return self.binarySearchRightBoundary(s, key, low, middle - 1)
        else:
            return self.binarySearchRightBoundary(s, key, middle + 1, high)

    def binarySearchLeftBoundary(self, s, key, low, high):
        if low > high:
            return low
        middle = low + (high - low) // 2
        middle_val = s[middle]
        if s[middle] < key:
            return self.binarySearchLeftBoundary(s, key, middle + 1, high)
        else:
            return self.binarySearchLeftBoundary(s, key, low, middle - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.countOccurences([-1, 0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 10, 11, 12, 13, 14], 4))
    # print(s.countOccurences([0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 10, 11, 12, 13, 14], -1))
