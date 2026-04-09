class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        u = UnionFind(n)
        for n1, n2 in edges:
            if not u.add(n1,n2):
                return False

        return True

class UnionFind:
    def __init__(self, n):
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
    
    def add(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            return True
        
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            return True

        self.par[p1] = p2
        self.rank[p2] += 1
        return True 