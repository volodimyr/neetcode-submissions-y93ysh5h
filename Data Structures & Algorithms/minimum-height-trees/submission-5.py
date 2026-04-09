class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        edgecount = {}
        leaves = deque()

        for v, neighs in adj.items():
            if len(neighs) == 1:
                leaves.append(v)
            edgecount[v] = len(neighs)
        
        while leaves:
            if n <= 2:
                break
            for _ in range (len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for neigh in adj[leaf]:
                    edgecount[neigh] -= 1
                    if edgecount[neigh] == 1:
                        leaves.append(neigh)
        return list(leaves)




