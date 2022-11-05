class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        l = len(s)
        if l != len(t):
            return False

        i = 0
        d1 = {}
        d2 = {}
        while i < l:
            if s[i] not in d1:
                d1[s[i]] = t[i]
            if t[i] not in d2:
                d2[t[i]] = s[i]
            if d1[s[i]] != t[i]:
                return False
            if len(d1) != len(d2):
                return False
            i += 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic('paper', 'title'))
    print(s.isIsomorphic('egg', 'add'))
    print(s.isIsomorphic('foo', 'bar'))
    print(s.isIsomorphic('badc', 'baba'))
    print(s.isIsomorphic('a','a'))
    print(s.isIsomorphic('egcd', 'adfd'))
