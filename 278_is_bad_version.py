# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool


class Solution(object):
    call_count = 0

    def isBadVersion(self, version):
        self.call_count += 1
        b = True
        if version >= 4:
            b = False
        v = 'Bad' if b is False else 'Good'
        print(str(version) + ' is ' + v + ' version, bad version is: ' + str(not b))
        return not b

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1
        k = n
        while i < k:
            j = i + (k - i) // 2
            if self.isBadVersion(j):
                # mid is bad version, then check left side (..], update the end pointer
                k = j
            else:
                # mid is good version, then check right side [+1..], update from the front pointer
                i = j + 1

        return i





if __name__ == '__main__':
    s = Solution()
    print(s.firstBadVersion(5))
