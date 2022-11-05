import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        _stones = [-x for x in stones]
        heapq.heapify(_stones)
        while len(_stones) > 1:
            heapq.heappush(_stones, heapq.heappop(_stones) - heapq.heappop(_stones))
        return -_stones[0]


if __name__ == '__main__':
    s = Solution()
    print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
