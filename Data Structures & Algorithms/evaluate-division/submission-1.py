class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        for (src, dst), weight in zip(equations, values):
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append((dst, weight))
            adj[dst].append((src, 1/weight))
        
        arr = []

        def dfs(src, target, visit):
            if src not in adj:
                return -1
            if target not in adj:
                return -1
            if src == target:
                return 1
            
            visit.add(src)
            for neigh, weight in adj[src]:
                if neigh not in visit:
                    res = dfs(neigh, target, visit)
                    if res != -1:
                        return weight * res
            return -1
        
        for src, target in queries:
            arr.append(dfs(src, target, set()))


        return arr
