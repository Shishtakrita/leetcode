from typing import List


def validIPAddress(s: str):

    def is_valid_range(num: str) -> bool:
        if 0 <= int(num) <= 255:
            if not (num[0] == '0' and len(num) > 1):
                return True
        return False

    def validIPHelper(soFar: str, remainingText: str, remainingPeriods: int, results: List[str]):
        print('soFar: {0}, remainingText:{1}, remainingPeriods:{2}, results: {3}'.format(soFar, remainingText,
                                                                                         remainingPeriods, results))

        if remainingPeriods == 0 and remainingText != '':
            if is_valid_range(remainingText):
                    results.append((soFar + '.' + remainingText)[1:])
        elif remainingText == '' or remainingPeriods < 0:
            pass
        elif len(remainingText) > (remainingPeriods + 1) * 3:
            pass
        else:
            for i in range(1, 4):
                soFarNext = remainingText[0:i]
                if is_valid_range(soFarNext):
                        validIPHelper(soFar + '.' + soFarNext, remainingText[i:], remainingPeriods - 1, results)
        return results

    results = validIPHelper('', s, 3, [])
    return results


print(validIPAddress("25511134255"))
# print(validIPAddress("123123123"))
# print(validIPAddress("572438139"))
# print(validIPAddress("1312140202"))
# print(validIPAddress("10001"))
# print(validIPAddress("0000"))
# print(validIPAddress("1234"))
# print(validIPAddress("45256137389"))
# print(validIPAddress("00001"))
# print(validIPAddress("123"))
