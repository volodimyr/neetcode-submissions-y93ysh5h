class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cps = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        while i < len(cps) and cps[i][0] <= w:
            heapq.heappush(max_heap, -cps[i][1])
            i+=1
        
        while k:
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
            while i < len(cps) and cps[i][0] <= w:
                heapq.heappush(max_heap, -cps[i][1])
                i+=1
            k-=1


        return w