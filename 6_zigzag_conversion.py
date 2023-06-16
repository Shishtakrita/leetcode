class Solution:
    def convert(self, s: str, numRows: int) -> str:

        str_list = [''] * numRows

        row_direction = 1
        index = 0
        for e in s:
            str_list[index] += e
            if numRows > 1:
                if index == numRows - 1:
                    row_direction = -1
                if index == 0:
                    row_direction = 1
                index += row_direction

        print(''.join(str_list))
        return ''.join(str_list)


if __name__ == '__main__':
    s = Solution()
    s.convert('PAYPALISHIRING', 4)
    s.convert('AB', 1)
