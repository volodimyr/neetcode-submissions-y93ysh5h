class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        nqueries = []
        m = {}
        i = 0
        for q in queries:
            m[q] = None
            nqueries.append((q, i))
            i += 1
        nqueries.sort()
        intervals.sort()

        div = deque(intervals)

        res = [-1]*len(queries)
        for q, pos in nqueries:
            if m[q] is not None:
                res[pos] = m[q]
                continue
            
            while div and q > div[0][0] and not (div[0][0] <= q <= div[0][1]):
                div.popleft()

            if not div:
                continue

            minres = math.inf
            for iv in div:
                if iv[0] <= q <= iv[1]:
                    minres = min(minres, iv[1]-iv[0]+1)
                if q < iv[0]:
                    break

            res[pos] = minres if minres != math.inf else -1

        return res
            

