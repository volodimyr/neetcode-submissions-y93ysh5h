class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)

        res = [-1] * n
        h = []
        for i in range(n):
            for j in range(m):
                p1x, p1y = bikes[j]
                p2x, p2y = workers[i]
                mnh = abs(p1x-p2x) + abs(p1y-p2y)
                heapq.heappush(h, (mnh, i, j))
        
        added = set()
        while h:
            _, worker, bike = heapq.heappop(h)
            if res[worker] != -1:
                continue
            if bike not in added:
                added.add(bike)
                res[worker] = bike
        return res