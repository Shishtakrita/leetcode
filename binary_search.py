from typing import List


def binary_search_left(arr: List[int], x: int) -> (int, int):
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        print('Reset Mid:: lo={},mid={},hi={}'.format(lo, mid, hi))
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
        print('Adjust Bounds:: lo={},mid={},hi={}'.format(lo, mid, hi))
    return lo, hi


def binary_search_right(arr: List[int], x: int) -> (int, int):
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        print('Reset Mid:: lo={},mid={},hi={}'.format(lo, mid, hi))
        if arr[mid] > x:
            hi = mid - 1
        else:
            lo = mid
        print('Adjust Bounds:: lo={},mid={},hi={}'.format(lo, mid, hi))
    return lo, hi


def binary_search2(arr: List[int], x: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        print('lo={},mid={},hi={}'.format(lo, mid, hi))
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid

    return lo if arr[lo] == x else -1


print('Binary Search 1....')
print(binary_search_left(
    arr=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    x=2))
print(binary_search_right(
    arr=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    x=2))

# print('\n\n\nBinary Search 2....')
# print(binary_search2(arr=[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], x=2))
