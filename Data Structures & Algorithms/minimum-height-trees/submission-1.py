class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        minheight = {i: float('inf') for i in range(n)}
        
        def dfs(n, root, visit, height):
            visit.add(n)
            bottom = True
            for neigh in adj[n]:
                if neigh not in visit:
                    bottom = False
                    dfs(neigh, root, visit, height+1)
            if bottom and minheight[root] == float('inf'):
                minheight[root] = height
            if bottom and minheight[root] != float('inf'):
                minheight[root] = max(height, minheight[root])
        
        minimal = float('inf')
        for i in range(n):
            dfs(i, i, set(), 0)
            if minimal > minheight[i]:
                minimal = minheight[i]

        
        res = []
        for n, h in minheight.items():
            if h == minimal:
                res.append(n)
        
        return res

