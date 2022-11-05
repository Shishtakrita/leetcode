from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)

        ans = []
        l = 0
        for r, char in enumerate(s):
            cnt[char] -= 1
            while cnt[char] < 0:  # If number of characters `char` is more than our expectation
                cnt[s[l]] += 1  # Slide left until cnt[char] == 0
                l += 1
            if r - l + 1 == len(p):  # If we already filled enough `p.length()` chars
                ans.append(l)  # Add left index `l` to our result

        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.findAnagrams('cbaebabacd', 'abc'))
    print(s.findAnagrams('abab', 'ab'))