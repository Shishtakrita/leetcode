from typing import List


def canBalance(target: int, weights: List[int]) -> bool:
    def helper(leftWeight: int, rightWeight: int, availableWeights: List[int]):
        if leftWeight + rightWeight == 0:
            return True
        elif not availableWeights:
            return False
        else:
            for i in range(len(availableWeights)):
                currentWeight = availableWeights[i]
                availableWeights.pop(i)
                if helper(leftWeight, rightWeight + currentWeight, availableWeights):
                    return True
                if helper(leftWeight - currentWeight, rightWeight, availableWeights):
                    return True
                availableWeights.insert(i, currentWeight)
            return False

    return helper(-target, 0, weights)


print(canBalance(5, [2, 5, 6]))
