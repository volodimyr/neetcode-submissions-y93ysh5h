class UnionFind:
    def __init__(self, accounts: List[List[str]]):
        self.par = {}
        self.rank = {}
        self.names = {}

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                self.names[accounts[i][j]] = accounts[i][0]
                self.par[accounts[i][j]] = accounts[i][j]
                self.rank[accounts[i][j]] = 0
    
    def find(self, x: str) -> str:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def add(self, x1: str, x2: str):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2]+=1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = UnionFind(accounts)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if len(accounts[i]) == 2:
                    continue
                if len(accounts[i]) == j+1:
                    continue
                union.add(accounts[i][j], accounts[i][j+1])
        
        comps = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                p = union.find(accounts[i][j])
                if p not in comps:
                    comps[p] = set()
                comps[p].add(accounts[i][j]) 

        res = []
        for p, emails in comps.items():
            sub = [union.names[p]]
            for email in emails:
                sub.append(email)
            res.append(sub)

        return res