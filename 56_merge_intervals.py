from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        li, prev = [], intervals[0]
        for curr in intervals[1:]:
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                li.append(prev)
                prev = curr

        li.append(prev)
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge(intervals=[[4, 5], [1, 4]]))
    print(s.merge(intervals=[[1, 4], [0, 4]]))
