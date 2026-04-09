class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        def dfs(node, par):
            height = 0
            for neigh in adj[node]:
                if neigh == par:
                    continue
                height = max(height, 1 + dfs(neigh, node))
            return height

        res = []
        minh = n
        for i in range(n):
            height = dfs(i, i)
            if minh == height:
                res.append(i)
            elif height < minh:
                minh = height
                res = [i]
        
        return res


