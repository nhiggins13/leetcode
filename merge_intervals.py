from operator import itemgetter


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=itemgetter(0))

        results = []

        for curr in intervals:
            if not results or results[-1][1] < curr[0]:
                results += [curr]
            else:
                results[-1][1] = max(curr[1], results[-1][1])

        return results