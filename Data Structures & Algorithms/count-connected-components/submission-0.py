class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        self.n = n
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def count_components(self)-> int:
        comps = set()
        for i in range(self.n):
            comps.add(self.find(i))
        return len(comps)
    
    def find(self, x: int)-> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def add(self, n1:int, n2:int):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            return
        
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            return
        
        self.par[p1] = p2
        self.rank[p2] += 1
        return
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for i in range(len(edges)):
            n1, n2 = edges[i][0], edges[i][1]
            uf.add(n1,n2)
        return uf.count_components()
