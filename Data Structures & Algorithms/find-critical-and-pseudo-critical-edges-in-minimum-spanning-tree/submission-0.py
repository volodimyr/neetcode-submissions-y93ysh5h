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

        def find_mst(exclude=-1, include=-1):
            h = []
            weight = 0
            count = 0
            u = UnionFind(n)

            if include != -1:
                _, n1, n2, w = edges[include]
                weight += w
                count += 1
                u.union(n1, n2)

            for i in range(len(edges)):
                if i == exclude:
                    continue
                _, n1, n2, w = edges[i]
                heapq.heappush(h, [w, n1, n2])
            
           
            while count < n-1:
                if not h:
                    return math.inf
                w, n1, n2 = heapq.heappop(h)
                if not u.union(n1, n2):
                    continue
                weight += w
                count += 1

            return weight

        base_weight = find_mst()
        
        for i in range(len(edges)):
            if find_mst(exclude=i) > base_weight:
                critical.append(i)
            elif find_mst(include=i) == base_weight:
                pseudo.append(i)
        
        return [critical, pseudo]


