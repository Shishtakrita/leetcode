class Solution:
    def method1(self):
        x = 4
        y = 20
        ans = []
        print('s:', x)

        def sub_method1(x):
            x = x + 2
            print('x in sub_method:', x, y)
            ans.append(1)

        sub_method1(x)
        sub_method1(x)
        sub_method1(x)

        print('x in method1:', x)
        print('ans', ans)


if __name__ == '__main__':
    s = Solution()
    s.method1()



