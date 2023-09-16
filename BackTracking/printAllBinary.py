from builtins import int


def printAllBinary(n: int):
    def printAllBinaryHelper(digits: str, size: int):
        if size == 0:
            print(digits)
            return
        else:
            printAllBinaryHelper(digits + "0", size - 1)
            printAllBinaryHelper(digits + "1", size - 1)

    printAllBinaryHelper("", n)


printAllBinary(2)
