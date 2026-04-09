class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [[1,0],[1,2],[3,1],[2,3],[2,4],[4,5],[2,5]]

        adjlist = {}
        for a, b in prerequisites:
            if b not in adjlist:
                adjlist[b] = []
            if a in adjlist:
                adjlist[a].append(b)
            else:
                adjlist[a] = [b]
        
        def has_cycle(node:int, path: deque)->bool:
            if node in path:
                return True
            neighbors = adjlist[node]
            if not neighbors:
                return False
            path.append(node)
            for n in neighbors:
                if has_cycle(n, path):
                    return True
            path.pop()
        
        for a in adjlist:
            if has_cycle(a, deque()):
                # if cycle exists then we cannot finish courses
                return False

        return True