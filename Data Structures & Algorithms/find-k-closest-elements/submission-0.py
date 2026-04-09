class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        for i, n in enumerate(arr):
            howclose = abs(n-x)
            heapq.heappush(min_heap, (howclose, i))
        
        res = []
        for i in range(k):
            res.append(arr[heapq.heappop(min_heap)[1]])
        
        return sorted(res)