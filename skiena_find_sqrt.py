class Solution:
    def squareRoot(self, num):
        return self.binarySearch(num, 1, num)

    def binarySearch(self, num, low, high):

        if low > high:
            return high, low

        middle = low + (high - low) // 2
        square = middle * middle
        if square == num:
            return middle
        if square > num:
            return self.binarySearch(num, low, middle - 1)
        else:
            return self.binarySearch(num, middle + 1, high)


if __name__ == '__main__':
    s = Solution()
    print(s.squareRoot(64))
