from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_map = {}
        for i, v in enumerate(order):
            order_map[v] = i

        print(order_map)
        for i in range(0, len(words) - 1):
            next_word_len = len(words[i + 1])
            for j in range(0, len(words[i])):
                if j >= next_word_len:
                    return False
                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                    break

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
    # print(s.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
