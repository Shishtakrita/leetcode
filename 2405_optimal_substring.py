class Solution:
    def partitionString(self, s: str) -> int:

        seen = 0
        partition = 1
        for e in s:
            val = ord(e) - ord('a')
            bit = 1 << val
            if seen & bit != 0:
                partition += 1
                seen = 0
            seen |= bit

        return partition

    def partitionString_array(self, s: str) -> int:

        last_seen = [-1] * 26
        prev_partition_end = -1
        partitions = 0

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')

            # if char already occurred in current work in progress partition
            if last_seen[index] >= prev_partition_end:
                partitions += 1
                prev_partition_end = i  # set the end point for the previous partition

            # update last seen position of the char
            last_seen[index] = i

        return partitions


s = Solution()
# print(s.partitionString(s="abacaba"))
print(s.partitionString_array(s="ssssss"))
