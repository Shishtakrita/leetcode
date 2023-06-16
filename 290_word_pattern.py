class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        str_parts = s.split(' ')

        if len(pattern) != len(str_parts):
            return False

        d1 = {}
        d2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in d1:
                d1[pattern[i]] = str_parts[i]
            if str_parts[i] not in d2:
                d2[str_parts[i]] = pattern[i]
            if d1[pattern[i]] != str_parts[i] or d2[str_parts[i]] != pattern[i]:
                return False

        print(d1, d2)

        return True


s = Solution()
print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(s.wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(s.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))


