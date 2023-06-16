class Solution:
    def permute_strings(self, s1: str) -> list:

        chosen = []
        self.permuteHelper(list(s1), chosen)

    def permuteHelper(self, l, chosen):
        if len(l) == 0:
            print(chosen)
        else:
            for k, v in enumerate(l):
                c = l[k]
                l.pop(k)
                chosen.append(c)
                self.permuteHelper(l, chosen)
                chosen.pop(len(chosen)-1)
                l.insert(k, c)


if __name__ == '__main__':
    s = Solution()
    s.permute_strings('xuumbjffxuzovdwrnolopeingppzgorotzdqfprokkmucxwsub')




