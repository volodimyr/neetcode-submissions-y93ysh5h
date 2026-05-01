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
    
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        uf = UnionFind(ROWS)
        for r in range(ROWS):
            for c in range(r + 1, ROWS):
                if isConnected[r][c] == 1:
                    uf.add(r, c)
        
        return uf.count_components()
