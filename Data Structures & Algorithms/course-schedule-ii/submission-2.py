class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        

        def dfs(n, path) -> bool:
            if n in path:
                return False
            if n in visit:
                return True
            visit.add(n)
            path.add(n)
            for p in adj[n]:
                if not dfs(p, path):
                    return False
            res.append(n)
            path.remove(n)
            return True
        
        res = []
        visit = set()
        for n in range(numCourses):
            if not dfs(n, set()):
                return []
            
        return res