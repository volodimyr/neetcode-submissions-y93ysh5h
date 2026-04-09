class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minheap = []
        for i in range (1, len(points)):
            dist = distance(points[0][0], points[0][1], points[i][0], points[i][1])
            heapq.heappush(minheap, (dist, points[i][0], points[i][1]))
        
        visit = set()
        total = 0
        visit.add((points[0][0], points[0][1]))
        while minheap:
            d, x, y = heapq.heappop(minheap)
            if (x,y) in visit:
                continue
            visit.add((x,y))
            total += d
            if len(visit) == len(points):
                return total
            for x1, y1 in points:
                if (x1,y1) not in visit:
                    dist = distance(x,y,x1,y1)
                    heapq.heappush(minheap, (dist, x1, y1))
        
        return 0


def distance(x1, y1, x2, y2) -> int:
    return abs(x1-x2) + abs(y1-y2)