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

        for src, target in queries:
            if target not in adj:
                arr.append(-1.0)
                continue

            q = deque()
            q.append((src, 1))
            res = -1

            visit = set()
            while q:
                s, weight = q.popleft()
                if s not in adj:
                    continue
                if s == target:
                    res = weight
                    break
                
                visit.add(s)
                for neigh, weight1 in adj[s]:
                    if neigh not in visit:
                        q.append((neigh, weight*weight1))
            
            arr.append(res)

        return arr