class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if  s is a subsequence of t

        lens = len(s)
        lent = len(t)

        if lens > lent:
            return False

        if lens == 0:
            return True

        sptr = 0
        sequence = 0
        for tptr in range(0, lent):
            if sptr > lens - 1:
                break
            if s[sptr] == t[tptr]:
                sequence += 1
                sptr += 1

        return sequence == lens