from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            0: '',
            1: '',
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        results = []

        def helper(soFar: str, currentDigitIndex: int):
            print('soFar={0}, currentDigitIndex={1}'.format(soFar, currentDigitIndex))
            if len(soFar) == len(digits):
                results.append(soFar)
            elif currentDigitIndex > len(digits) - 1:
                return
            else:
                numVal = digits[currentDigitIndex]
                chars = letter_map[int(numVal)]
                for i in range(len(chars)):
                    helper(soFar + chars[i], currentDigitIndex + 1)
            return results


        results = helper('', 0)
        return results


s = Solution()
print(s.letterCombinations(digits="234"))
