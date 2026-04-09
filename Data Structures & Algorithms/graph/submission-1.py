class Graph:
    def __init__(self):
        self.nodes = {}

    def addEdge(self, src: int, dst: int) -> None:
        neighbours = []
        if src in self.nodes:
            neighbours = self.nodes[src]
        if dst not in neighbours:
            neighbours.append(dst)
            self.nodes[src] = neighbours
        if dst not in self.nodes:
            self.nodes[dst] = []

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.nodes:
            return False
        neighbours = self.nodes[src]
        if dst not in neighbours:
            return False
        neighbours.remove(dst)
        self.nodes[src] = neighbours
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src == dst:
            return True
        visit = set()
        q = deque(self.nodes[src])
        while q:
            neighbour = q.popleft()
            if neighbour in visit:
                continue
            if neighbour == dst:
                return True
            visit.add(neighbour)
            for n in self.nodes[neighbour]:
                q.append(n)
        return False