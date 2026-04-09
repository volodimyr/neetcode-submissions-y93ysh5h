class UnionFind:
    def __init__(self, n):
        self.rank = {}
        self.par = {}
        for i in range(n):
            self.rank[i] = 0
            self.par[i] = i
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
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


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [[i, n1, n2, w] for i, (n1, n2, w) in enumerate(edges)]
        critical = []
        pseudo = []
        edges.sort(key=lambda x: x[3])

        def find_mst(exclude=-1, include=-1):
            weight = 0
            count = 0
            u = UnionFind(n)

            if include != -1:
                _, n1, n2, w = edges[include]
                weight += w
                count += 1
                u.union(n1, n2)            
           
            for i, (_, n1, n2, w) in enumerate(edges):
                if i == exclude:
                    continue
                if u.union(n1, n2):
                    weight += w
                    count += 1
                if count == n - 1:
                    break

            return weight if count == n-1 else math.inf

        base_weight = find_mst()
        
        for i in range(len(edges)):
            if find_mst(exclude=i) > base_weight:
                critical.append(edges[i][0])
            elif find_mst(include=i) == base_weight:
                pseudo.append(edges[i][0])
        
        return [critical, pseudo]


