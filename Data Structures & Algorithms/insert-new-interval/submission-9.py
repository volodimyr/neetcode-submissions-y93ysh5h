class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if ni[1] < interval[0]:
                return res + [ni] + intervals[i:]
            if ni[0] > interval[1]:
                res.append(interval)
            else:
                ni = [min(interval[0], ni[0]), max(interval[1], ni[1])]

        res.append(ni)

        return res