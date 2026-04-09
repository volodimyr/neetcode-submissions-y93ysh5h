class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        res = []
        adj = {i : [] for i in range(n)}
        for src, dst, weight in edges:
            adj[src].append((dst, weight))
            adj[dst].append((src, weight)) 
        minheap = [(0, 0)]
        visit = set()
        while minheap:
            weight, src = heapq.heappop(minheap)
            if src in visit:
                continue
            visit.add(src)
            res.append(weight)
            if len(res) == n:
                return sum(res)
            for src1, weight1 in adj[src]:
                if src1 not in visit:
                    heapq.heappush(minheap, (weight1, src1))

        return -1

