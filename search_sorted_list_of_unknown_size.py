# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low = 0
        high = 10000
        out_of_bounds = 2147483647

        while (low <= high):
            mid = (high + low) // 2

            val = reader.get(mid)

            if val == target:
                return mid
            elif mid == 0:
                return -1
            elif val == out_of_bounds or val > target:
                high = mid - 1
            elif val < target:
                low = mid + 1

        return -1