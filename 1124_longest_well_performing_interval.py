from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        tiring_count = 0
        weak_count = 0
        prevInterval = 0
        currInterval = 0

        for i in hours:
            if i > 8:
                tiring_count += 1
            else:
                weak_count += 1

            prevInterval = max(currInterval, prevInterval)
        return prevInterval


if __name__ == '__main__':
    s = Solution()
    print(s.longestWPI([9, 9, 6, 0, 6, 6, 9]))
    print(s.longestWPI([6, 6, 6]))
    print(s.longestWPI([6, 6, 9]))
    print(s.longestWPI([9, 6, 9]))
