class Solution(object):
    # https: // www.youtube.com / watch?v = G8xtZy0fDKg

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        pCounts = {}
        sCounts = {}
        for i in range(len(p)):
            pCounts[p[i]] = 1 + pCounts.get(p[i], 0)
            sCounts[s[i]] = 1 + sCounts.get(s[i], 0)

        res = [0] if pCounts == sCounts else []
        l = 0
        for r in range(len(p), len(s)):
            sCounts[s[r]] = 1 + sCounts.get(s[r], 0)
            sCounts[s[l]] -= 1

            if sCounts[s[l]] == 0:
                sCounts.pop(s[l])
            l += 1
            if sCounts == pCounts:
                res.append(l)

        return res





        return anagram_pos


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams('cbaebabacd', 'abc'))
    print(s.findAnagrams('abab', 'ab'))
