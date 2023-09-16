from typing import List


def diceSum(dice_count: int, target_sum: int):
    def diceSumHelper(dice_count: int, target_sum: int, dice_left: int, curr_sum: int, dice_option: List[int],
                      results: set[list[int]]):

        if dice_left == 0 and curr_sum == target_sum:
            results.add(list(sorted(dice_option[:])))
        elif (curr_sum + dice_left * 1) > target_sum or (curr_sum + dice_left * 6 < target_sum):
            # do nothing
            pass
        else:
            for i in range(1, 7):
                if curr_sum + i <= target_sum:
                    dice_option.append(i)
                    diceSumHelper(dice_count, target_sum, dice_left - 1, curr_sum + i, dice_option, results)
                    dice_option.pop()

        return results

    return diceSumHelper(dice_count, target_sum, dice_count, 0, [], set([]))


print(diceSum(3, 7))
