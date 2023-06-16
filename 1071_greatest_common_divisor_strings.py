# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        l1, l2 = len(str1), len(str2)

        def _is_valid(k: int) -> bool:
            if l1 % k or l2 % k:
                return False

            n1, n2 = l1 // k, l2 // k
            base = str1[:k]
            return str1 == base * n1 and str2 == base * n2

        for i in range(min(l1, l2), 0, -1):
            if _is_valid(i):
                return str1[:i]

        return ''


if __name__ == '__main__':
    s = Solution()
    print(s.gcdOfStrings('ABCABCABC', 'ABC'))
