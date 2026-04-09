class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adjlist[a].append(b)
        
        def has_cycle(node: int)->bool:
            if node in visit:
                # cycle detected
                return True
            if adjlist[node] == []:
                return False
            visit.add(node)
            for n in adjlist[node]:
                if has_cycle(n):
                    return True
            visit.remove(node)
            adjlist[node] = []
            return False
        
        visit = set()
        for c in range(numCourses):
            if has_cycle(c):
                # cannot complete all courses
                return False
        return True