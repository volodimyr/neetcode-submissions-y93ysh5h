class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        resh = [(-heights[len(heights)-1], len(heights)-1)]
        arr = [heights[len(heights)-1]]
        for i in range(len(heights)-2, -1, -1):
            if heights[i] <= arr[0]:
                continue
            else:
                arr[0] = heights[i]
                heapq.heappush(resh, (-heights[i], i))

        res = []
        while resh:
            res.append(heapq.heappop(resh)[1])
        
        return res