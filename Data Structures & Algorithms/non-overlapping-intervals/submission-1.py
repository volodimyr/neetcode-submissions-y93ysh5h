class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort()
        _, prevEnd = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if prevEnd > start:
                res+=1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        return res