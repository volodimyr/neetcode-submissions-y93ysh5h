class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ni = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if ni[1] >= interval[0]:
                ni = [min(interval[0], ni[0]), max(interval[1], ni[1])]
            else:
                res.append(ni)
                ni = interval
        res.append(ni)
        return res