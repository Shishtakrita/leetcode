class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        secretST = {}
        guessST = {}
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            secret_char = secret[i]
            guess_char = guess[i]
            if secret_char == guess_char:
                bulls += 1
            else:
                if secret_char in secretST:
                    secretST[secret_char] += 1
                else:
                    secretST[secret_char] = 1

                if guess_char in guessST:
                    guessST[guess_char] += 1
                else:
                    guessST[guess_char] = 1

                if guess_char in secretST:
                    if secretST[guess_char] > 0:
                        cows += 1
                        secretST[guess_char] -= 1
                        guessST[guess_char] -= 1

                if secret_char in guessST:
                    if guessST[secret_char] > 0:
                        cows += 1
                        guessST[secret_char] -= 1
                        secretST[secret_char] -= 1

        return str(bulls) + "A" + str(cows) + "B"


if __name__ == '__main__':
    s = Solution()
    print(s.getHint("1123", "0111"))
    print(s.getHint("1807", "7810"))
    print(s.getHint("2962", "7236"))


