from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        pairs = []
        no_pairs = []
        pair_maps = {}

        for word in words:
            if word in pair_maps:
                pairs.append(word)
            else:
                no_pairs.append(word)

