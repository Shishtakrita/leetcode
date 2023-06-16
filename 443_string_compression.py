from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        res = []
        prev = ''
        cnt = 1
        for i in range(len(chars)):
            s = chars[i]
            if s == prev:
                cnt += 1
            else:
                cnt = 1
            prev = s
            print('{},{}'.format(prev, cnt))

if __name__ == '__main__':
     s = Solution()
     s.compress(chars = ["a","a","b","b","c","c","c"])




