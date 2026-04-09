class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], start: int, end: int, k: int) -> int:
        adj = {i : [] for i in range (n)}
        for s, d, c in flights:
            adj[s].append((d, c))
        
        minheap = [(0, 0, start)]
        res = []
        visit = set()
        while minheap:
            cost1, stops, src1 = heapq.heappop(minheap)
            if src1 == end:
                res.append(cost1)
                continue
            if stops > k:
                continue
            if src1 in visit and res and min(res) < cost1:
                continue
            visit.add(src1)

            for src2, cost2 in adj[src1]:
                if src2 in visit and res and min(res) < cost1+cost2:
                    continue
                heapq.heappush(minheap, (cost1+cost2, stops+1, src2))
        if not res:
            return -1
        return min(res)
