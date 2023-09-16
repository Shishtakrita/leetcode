from typing import List


def permuteString(s: str):
    def permuteHelper(soFar: str, rest: str, results: List[str]):
        print(soFar, rest)
        if rest == "":
            results.append(soFar)
        else:
            for i in range(len(rest)):
                next = soFar + rest[i]
                remaining = rest[0: i] + rest[i + 1:]
                permuteHelper(next, remaining, results)

        return results

    return permuteHelper("", s, [])


print(permuteString("abcd"))
