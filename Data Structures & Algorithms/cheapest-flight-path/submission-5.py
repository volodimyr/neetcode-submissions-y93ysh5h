class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], start: int, end: int, k: int) -> int:
        adj = {i : [] for i in range (n)}
        for s, d, c in flights:
            adj[s].append((d, c))
        prices = [float("inf")] * n
        prices[start] = 0
        
        q = deque()
        q.append((0, 0, start))
        while q:
            cost1, stops, src1 = q.popleft()
            if stops > k:
                continue
            for src2, cost2 in adj[src1]:
                ncost = cost1+cost2
                if ncost < prices[src2]:
                    q.append((ncost, stops+1, src2))
                    prices[src2] = ncost
                
        return prices[end] if prices[end] != float("inf") else -1