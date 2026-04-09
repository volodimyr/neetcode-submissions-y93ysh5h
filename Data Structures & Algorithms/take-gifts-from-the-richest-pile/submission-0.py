import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        mh = []
        for g in gifts:
            heapq.heappush(mh, -g)
        
        for _ in range(k):
            n = -(heapq.heappop(mh))
            n = math.sqrt(n)
            heapq.heappush(mh, int(-n))
        
        res = []
        for n in mh:
            res.append(-n)

        return sum(res)