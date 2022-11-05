class Solution:
    def reverseVowels(self, s: str) -> str:

        low, high = 0, len(s) - 1
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

        while True:
            while s[low] not in vowels and low < high:
                low += 1
            while s[high] not in vowels and low < high:
                high -= 1

            if low >= high:
                break

            s = s[:low] + s[high] + s[low + 1:high] + s[low] + s[high + 1:]
            low += 1
            high -= 1

        return s


if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels('aA'))
