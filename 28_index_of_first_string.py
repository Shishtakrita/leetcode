class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        len_h = len(haystack)
        len_n = len(needle)

        if len_h < len_n:
            return -1

        for i in range(len_h - len_n + 1):
            for j in range(len_n):
                if haystack[i+j] != needle[j]: break
                if j == len_n - 1: return i

        return -1


if __name__ == '__main__':
    s = Solution()
    # print(s.strStr(haystack="sadbutsad", needle="sad"))
    print(s.strStr(haystack="mississippi", needle="a"))
