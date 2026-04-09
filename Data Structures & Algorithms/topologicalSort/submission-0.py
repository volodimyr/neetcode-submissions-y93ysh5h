class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range (n)}
        for src, dst in edges:
            adj[src].append(dst)
        
        
        def dfs(n) -> bool:
            if n in path:
                return False
            if n in visit:
                return True
            path.add(n)
            visit.add(n)
            for n1 in adj[n]:
                if not dfs(n1):
                    return False
            res.append(n)
            path.remove(n)
            return True

        res = []
        visit = set()
        path = set()
        for i in range(n):
            if not dfs(i):
                return []
        res.reverse()
        return res