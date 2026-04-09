class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            if ni[1] < interval[0]:
                res.append(ni)
                res.extend(intervals[intervals.index(interval):])
                return res
            if ni[0] > interval[1]:
                res.append(interval)
            else:
                ni = self.merge(ni, interval)

        res.append(ni)

        return res
    
    def merge(self, i1, i2):
        merged = []
        merged.append(min(i1[0], i2[0]))
        merged.append(max(i1[1], i2[1]))
        return merged