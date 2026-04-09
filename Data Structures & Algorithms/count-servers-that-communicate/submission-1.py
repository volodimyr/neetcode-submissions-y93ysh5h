class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        rcnt = [0] * ROWS
        ccnt = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rcnt[r] +=1
                    ccnt[c] += 1
        
            
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and max(rcnt[r], ccnt[c]) > 1:
                    res+=1

        return res