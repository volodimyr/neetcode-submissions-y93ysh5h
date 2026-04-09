"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        res = [[intervals[0]]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            added = False
            for rows in res:
                rcur = rows[-1]                
                if rcur.end <= cur.start:
                    rows.append(cur)
                    added = True
                    break
            if not added:
                res.append([cur])
                
        return len(res)
