class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i : [] for i in range(n)}
        for edge, succ in zip(edges, succProb):
            adj[edge[0]].append((edge[1], succ))
            adj[edge[1]].append((edge[0], succ))
        
        maxheap = [(float(-1), start_node)]
        highestProbability = {}
        while maxheap:
            prob1, src1 = heapq.heappop(maxheap)
            if src1 in highestProbability:
                continue
            highestProbability[src1] = prob1

            for src2, prob2 in adj[src1]:
                if src2 not in highestProbability:
                    heapq.heappush(maxheap, (prob2*prob1, src2))
        
        if end_node not in highestProbability:
            return float(0)
        prob = highestProbability[end_node]
        return -prob