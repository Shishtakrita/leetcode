# https://leetcode.com/problems/permutation-in-string/

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d1 = dict(Counter(s1))
        d2 = dict(Counter(s2))

        if not set(d1).issubset(set(d2)):
            return False

        for k in d1:
            if d1[k] > d2[k]:
                return False

        b = self.permute_helper(list(s1), [], s2)
        return bool(b)

    def permute_helper(self, l: list, chosen: list, s2: str) -> bool:
        if len(l) == 0:
            if ''.join(chosen) in s2:
                return True
        else:
            for k, v in enumerate(l):
                # choose
                c = l[k]
                l.pop(k)
                chosen.append(c)
                b = self.permute_helper(l, chosen, s2)
                if b:
                    return True
                # un choose
                chosen.pop(len(chosen) - 1)
                l.insert(k, c)


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion('ab', 'eidbaooo'))
    print(s.checkInclusion('ab', 'eidboaoo'))

