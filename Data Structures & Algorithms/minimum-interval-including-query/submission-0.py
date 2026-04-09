class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        nqueries = []
        m = {}
        i = 0
        for q in queries:
            m[q] = -1
            nqueries.append((q, i))
            i += 1
        nqueries.sort()
        intervals.sort()
        res = [-1]*len(queries)
        for q, pos in nqueries:
            if m[q] != -1:
                res[pos] = m[q]
            else:
                minres = math.inf
                for iv in intervals:
                    if iv[0] <= q <= iv[1]:
                        minres = min(minres, iv[1]-iv[0]+1)
                res[pos] = minres if minres != math.inf else -1

        return res
            

