
class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = set()
            self.adj[src].add(dst)
        elif dst not in self.adj[src]:
            self.adj[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj:
            return False
        if dst not in self.adj[src]:
            return False
        self.adj[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        def dfs(node):
            if node == dst:
                return True
            visit.add(node)
            if node not in self.adj:
                return False

            for n in self.adj[node]:
                if n not in visit:
                    if dfs(n):
                        return True
            return False
        
        return dfs(src)
    # def hasPath(self, src: int, dst: int) -> bool:
    #     visit = set()

    #     def dfs(node):
    #         if node == dst:
    #             return True
    #         visit.add(node)
    #         for n in self.adj.get(node, []):
    #             if n not in visit:
    #                 if dfs(n):
    #                     return True
    #         return False

    #     return dfs(src)
