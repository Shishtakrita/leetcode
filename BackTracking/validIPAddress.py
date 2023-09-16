from typing import List


def validIPAddress(ip: str):
    def validIPHelper(soFar: str, rest: str, remaining_periods: int, results: List[str]):
        # print(soFar, rest, remaining_periods)
        if remaining_periods == 0 and 1 <= len(rest) <= 3:
            if not (rest[0] == "0" and len(rest) != 1):
                results.append(soFar + rest)
        elif (remaining_periods == 1 and len(rest) > 6) or (
                remaining_periods == 2 and len(rest) > 9) or remaining_periods < 0:
            # do nothing
            return
        else:
            for i in range(1, 11):
                next = soFar + rest[:i]
                remaining = rest[i:]
                parts = next.split('.')
                if parts[-1] and 0 <= int(parts[-1]) <= 255:
                    if not (parts[-1][0] == "0" and len(parts[-1]) != 1):
                        validIPHelper(next + '.', remaining, remaining_periods - 1, results)
        return results

    return validIPHelper("", ip, 3, [])


print(validIPAddress("25511134255"))
print(validIPAddress("123123123"))
print(validIPAddress("572438139"))
print(validIPAddress("1312140202"))
print(validIPAddress("10001"))
print(validIPAddress("0000"))
print(validIPAddress("1234"))
print(validIPAddress("45256137389"))
print(validIPAddress("00001"))
print(validIPAddress("123"))
