class Solution:
    def addBinary(self, a: str, b: str) -> str:

            a_len = len(a)
            b_len = len(b)

            #  1011
            # 10101

            out_string = []
            for i in range(a_len - 1, -1, -1):
                a_val = int(a[i])
                if i <= b_len - 1:
                    b_val = int(b[i])
                else:
                    b_val = 0

                if a_val & b_val == 1:
                    out_string.append('1')
                    carry_over = 1
                elif a_val | b_val == 1:
                    out_string.append('1')
                    carry_over = 0
                else:
                    out_string.append('0')
                    carry_over = 0









