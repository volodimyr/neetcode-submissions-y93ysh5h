class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        h = []

        for i in intervals:
            if h and h[0] <= i.start:
                heapq.heappop(h)
            heapq.heappush(h, i.end)
        
        return len(h)