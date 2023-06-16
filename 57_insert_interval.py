from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        '''
        1. insert left intervals
        2. merge overlapping intervals
        3. insert right intervals
        '''

        if not intervals:
            return [newInterval]

        i, res = 0, []
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
    print(s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
    print(s.insert(intervals=[], newInterval=[5, 7]))
    print(s.insert(intervals=[[1, 5]], newInterval=[2, 3]))
