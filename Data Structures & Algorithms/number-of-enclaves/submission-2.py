class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def can(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return (True, 0)  
            if grid[r][c] == 0 or (r, c) in visit:
                return (False, 0)

            visit.add((r, c))

            touches = False
            size = 1
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r+dr, c+dc
                if (nr, nc) in visit:
                    continue
                t, s = can(nr, nc)
                if t:
                    touches = True
                size += s
            
            return (touches, size)
        
        visit = set()
        enclave = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                if (r,c) in visit:
                    continue
                t, s = can(r, c)
                if not t:
                    enclave += s

        return enclave

