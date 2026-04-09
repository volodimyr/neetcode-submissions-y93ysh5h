class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}
        for a, b in prerequisites:
            if b not in adjlist:
                adjlist[b] = []
            if a in adjlist:
                adjlist[a].append(b)
            else:
                adjlist[a] = [b]
        
        def has_cycle(node:int, path: deque, visit: set)->bool:
            if node in path:
                return True
            if node in visit:
                return False
            neighbors = adjlist[node]
            path.append(node)
            visit.add(node)
            for n in neighbors:
                if has_cycle(n, path, visit):
                    return True
            path.pop()
        
        visit = set()
        for a in adjlist:
            if has_cycle(a, deque(), visit):
                # if cycle exists then we cannot finish courses
                return False
        return True