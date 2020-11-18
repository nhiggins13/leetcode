import bisect
import itertools


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # check if totally inside range
        if intervals[0][0] >= toBeRemoved[0] and intervals[-1][1] < toBeRemoved[1]:
            return []

        flat = list(itertools.chain(*intervals))

        low = bisect.bisect_left(flat, toBeRemoved[0])
        high = bisect.bisect_left(flat, toBeRemoved[1])

        high_idx = high // 2
        low_idx = low // 2

        if low_idx == high_idx:
            if intervals[low_idx] == toBeRemoved:
                del intervals[low_idx]
            elif toBeRemoved[0] <= intervals[low_idx][0]:
                intervals[low_idx][0] = max(toBeRemoved[1], intervals[low_idx][0])
            else:
                interval_high = intervals[low_idx][1]
                intervals[low_idx][1] = toBeRemoved[0]
                intervals.insert(low_idx + 1, [toBeRemoved[1], interval_high])

            return intervals

        if high < len(flat):
            if high & 1:
                if high_idx + 1 < len(intervals) - 1 and intervals[high_idx + 1][0] == toBeRemoved[1] + 1:
                    high_idx += 1
                    intervals[high_idx][0] = max(toBeRemoved[1], intervals[high_idx][0])
                else:
                    intervals[high_idx][0] = toBeRemoved[1]
            else:
                intervals[high_idx][0] = max(toBeRemoved[1], intervals[high_idx][0])

        if low & 1:
            intervals[low_idx][1] = toBeRemoved[0]
            low_idx += 1

        return intervals[:low_idx] + intervals[high_idx:]