class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        r, c = 0, 0
        max_heap = [(-grid[r][c], r, c)]

        res = grid[r][c]
        
        visit = set()
        visit.add((r,c))
        while True:
            val, r, c = heapq.heappop(max_heap)
            val = -val
            res = min(res, val)
            if r == ROWS-1 and c == COLS-1:
                break
            
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = r+dr, c+dc
                if min(nr,nc) < 0:
                    continue
                if nr == ROWS or nc == COLS:
                    continue
                if (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                heapq.heappush(max_heap, (-grid[nr][nc], nr, nc))
        
        return res


