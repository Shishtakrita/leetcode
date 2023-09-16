def printDecimal(n: int):
    def printDecimalHelper(size: int, soFar: str):
        if size == 0:
            print(soFar)
        else:
            for i in range(0, 10):
                printDecimalHelper(size - 1, soFar + str(i))

    printDecimalHelper(n, "")


printDecimal(3)
