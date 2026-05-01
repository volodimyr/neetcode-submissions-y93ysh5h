class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = deque()
        res.append(len(heights)-1)
        arr = [heights[len(heights)-1]]
        for i in range(len(heights)-2, -1, -1):
            if heights[i] <= arr[0]:
                continue
            else:
                arr[0] = heights[i]
                res.appendleft(i)
        
        return list(res)