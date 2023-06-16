from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats(people=[3, 5, 3, 4], limit=5))
