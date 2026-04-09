class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        rem_start, rem_end = toBeRemoved[0], toBeRemoved[1]
        for i in range(len(intervals)):
            start, end = intervals[i]
            if end <= rem_start or start >= rem_end:
                res.append([start,end])
            else:
                if start < rem_start:
                    res.append([start,rem_start])
                if end > rem_end:
                    res.append([rem_end, end])
        
        return res