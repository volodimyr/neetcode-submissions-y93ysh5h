class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)     

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.points[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point[0], point[1]
        for k, count in self.points.items():
            x2, y2 = k[0], k[1]
            dx = x-x2
            dy = y-y2
            if dx == 0 or dy == 0:
                continue
            if abs(dx) != abs(dy):
                continue
            if (x,y2) in self.points and (x2,y) in self.points:
                res += (count * self.points[(x,y2)] * self.points[(x2,y)])

        return res
        