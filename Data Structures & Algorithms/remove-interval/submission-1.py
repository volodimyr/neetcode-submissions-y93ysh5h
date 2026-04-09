class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        def covered(a,b):
            return toBeRemoved[0] <= a and b <= toBeRemoved[1] 

        def partially(a, b):
                start = max(a, toBeRemoved[0])
                end = min(b, toBeRemoved[1])
                if start <= end:
                    return [start, end]
                
        res = []
        rem_start, rem_end = toBeRemoved[0], toBeRemoved[1]
        for i in range(len(intervals)):
            start, end = intervals[i]
            if end < rem_start or start > rem_end:
                res.append([start,end])
            else:
                if start < rem_start:
                    res.append([start,rem_start])
                if end > rem_end:
                    res.append([rem_end, end])
        
        return res