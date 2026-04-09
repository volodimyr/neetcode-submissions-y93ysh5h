class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        rooms = []
        for i in intervals:
            if rooms and rooms[0] <= i.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i.end)
        return len(rooms)