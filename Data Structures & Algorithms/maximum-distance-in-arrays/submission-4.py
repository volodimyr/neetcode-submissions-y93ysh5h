class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        res = 0
        for r in range(1, len(arrays)):
            res = max(res, max(abs(arrays[r][0]-max_val), abs(arrays[r][-1]-min_val)))
            min_val = min(min_val, arrays[r][0])
            max_val = max(max_val, arrays[r][-1])

        return res