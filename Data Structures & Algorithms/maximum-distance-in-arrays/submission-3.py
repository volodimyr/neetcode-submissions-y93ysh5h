class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ROWS = len(arrays)
        res = -math.inf
        for r in range(ROWS):
            n = arrays[r][0]
            for r1 in range(ROWS):
                if r1 == r:
                    continue
                res = max(res, abs(n - arrays[r1][len(arrays[r1])-1]))
        
        return res