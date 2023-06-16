from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        '''
        You are given two positive integer arrays spells and potions, of length n and m respectively,
        where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

        You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
        Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.


        Example 1:

        Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
        Output: [4,0,3]
        Explanation:
        - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
        - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
        - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
        Thus, [4,0,3] is returned.
        '''

        def binary_search(lo: int, hi: int, k: int) -> int:
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if potions[mid] < k:
                    lo = mid + 1
                else:
                    hi = mid
            return lo if potions[lo] >= k else -1

        potions = sorted(potions)
        l, h = 0, len(potions) - 1
        ans = []
        for i in range(len(spells)):
            min_potion_for_success = (success + spells[i] - 1) // spells[i]  # ceiling
            index = binary_search(l, h, min_potion_for_success)
            success_count = 0 if index == -1 else h - index + 1
            ans.append(success_count)

        return ans


s = Solution()
print(s.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
