class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minheap = []
        for src, dst, weight in edges:
            heapq.heappush(minheap, (weight, src, dst))
        
        union = UnionFind(n)
        total = 0

        connected = 0
        while minheap:
            weight, src, dst = heapq.heappop(minheap)
            if not union.add(src, dst):
                continue
            connected += 1
            total += weight
            if connected == n-1:
                return total

        return -1

class UnionFind:
    def __init__(self, n: int)-> 'UnionFind':
        self.n = n
        self.rank = {}
        self.par = {}
        for i in range(n):
            self.rank[i] = 0
            self.par[i] = i
    
    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def add(self, n1:int, n2:int)-> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True