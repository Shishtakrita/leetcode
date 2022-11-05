from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        ans = 0
        maxDefense = float('-inf')
        properties = sorted(properties, key=lambda x: (x[0], -x[1]))

        for i in range(len(properties) - 1, -1, -1):
            if properties[i][1] < maxDefense:
                ans += 1
            maxDefense = max(properties[i][1], maxDefense)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfWeakCharacters([[1, 5], [10, 4], [4, 3], [10, 20]]))
