class UnionFind:
    def __init__(self, n:int):
        self.par = {}
        self.rank = {}
        for i in range(1, n+1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def add(self, n1:int, n2:int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            # cycle
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for i in range(len(edges)):
            if not uf.add(edges[i][0], edges[i][1]):
                return [edges[i][0],edges[i][1]]
        return []