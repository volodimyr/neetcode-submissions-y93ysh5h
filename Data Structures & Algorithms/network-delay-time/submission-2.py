class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n+1)}
        for src, dst, t in times:
            adj[src].append((dst, t))
        minheap = []
        minheap = [(0, k)]
        shortest = {}
        res = 0
        while minheap:
            t1, src1 = heapq.heappop(minheap)
            if src1 in shortest:
                continue
            shortest[src1] = t1
            res = t1
            for src2, t2 in adj[src1]:
                if src2 not in shortest:
                    heapq.heappush(minheap, (t1+t2, src2))
        if len(shortest) != n:
            return -1
        return res      
            


