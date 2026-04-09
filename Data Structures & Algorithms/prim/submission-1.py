class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for src, dst, weight in edges:
            adj[src].append((dst, weight))
            adj[dst].append((src, weight)) 
        minheap = [(0, 0)]
        visit = set()
        total = 0
        while minheap:
            weight, src = heapq.heappop(minheap)
            if src in visit:
                continue
            visit.add(src)
            total += weight
            if len(visit) == n:
                return total
            for src1, weight1 in adj[src]:
                if src1 not in visit:
                    heapq.heappush(minheap, (weight1, src1))

        return -1

