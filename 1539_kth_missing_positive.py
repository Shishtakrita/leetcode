from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        if k < arr[0]:
            return k

        prev_num = 0
        missing_cnt = 0
        for i in range(len(arr)):
            curr_num = arr[i]
            if prev_num + 1 != curr_num:
                missing_cnt += curr_num - prev_num - 1
            # else:
            #     missing_cnt = 0
            if k <= missing_cnt:
                print('k={}, missing={}, prev_num={}'.format(k, missing_cnt, prev_num))
                return curr_num + k - missing_cnt - 1
            # k -= missing_cnt
            prev_num = curr_num

        return arr[-1] + k - missing_cnt


s = Solution()
print(s.findKthPositive(arr=[5, 6, 7, 8, 9], k=9))
# print(s.findKthPositive(arr=[1, 2, 3, 4], k=2))
# print(s.findKthPositive(arr=[1, 3], k=1))
