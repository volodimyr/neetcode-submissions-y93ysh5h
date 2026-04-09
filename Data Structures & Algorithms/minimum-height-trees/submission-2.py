class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        minheight = {i: 0 for i in range(n)}
        
        def dfs(node, root, visit, height):
            visit.add(node)
            minheight[root] = max(minheight[root], height)
            for neigh in adj[node]:
                if neigh not in visit:
                    dfs(neigh, root, visit, height + 1)
        
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

