class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = {}
        intervals.sort()
        hp = []
        i = 0

        for q in sorted(queries):
            if q in res:
                continue
            while i < len(intervals) and q >= intervals[i][0]:
                l, r = intervals[i]
                heapq.heappush(hp, (r-l+1, r))
                i += 1

            while hp and q > hp[0][1]:
                heapq.heappop(hp)
            
            res[q] = hp[0][0] if hp else -1

        return [res[q] for q in queries]
            

