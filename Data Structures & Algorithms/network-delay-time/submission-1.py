class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n+1)}
        for src, dst, t in times:
            adj[src].append((dst, t))
        minheap = []
        minheap = [(0, k)]
        shortest = {}
        while minheap:
            t1, src1 = heapq.heappop(minheap)
            if src1 in shortest:
                continue
            shortest[src1] = t1
            for src2, t2 in adj[src1]:
                if src2 not in shortest:
                    heapq.heappush(minheap, (t1+t2, src2))
        
        res = 0
        for i in range(1, n+1):
            if i not in shortest:
                return -1
            res = max(res, shortest[i])
        return res        
            


