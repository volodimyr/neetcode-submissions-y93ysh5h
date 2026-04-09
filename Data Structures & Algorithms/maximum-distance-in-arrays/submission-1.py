class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ROWS = len(arrays)
        res = -math.inf
        for r in range(ROWS):
            COLS = len(arrays[r])
            for c in range(COLS):
                n = arrays[r][c]
                for r1 in range(r+1, ROWS, 1):
                    for c1 in range(len(arrays[r1])):
                        res = max(res, abs(n - arrays[r1][c1]))
        
        return res