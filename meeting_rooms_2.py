import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        ordered = sorted(intervals)

        rooms = [ordered[0][1]]
        max_count = 1

        for start, end in ordered[1:]:

            if len(rooms) > 0 and start >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, end)

            max_count = max(max_count, len(rooms))

        return max_count