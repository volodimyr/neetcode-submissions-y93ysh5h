class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visits = set()
        
        def dfs(r: int, c: int) -> int:
            if r == ROWS or c == COLS:
                return 0
            if r < 0 or c < 0:
                return 0
            if (r,c) in visits:
                return 0
            if grid[r][c] == 1:
                return 0
            if r == ROWS-1 and c == COLS-1:
                return 1
            
            visits.add((r,c))

            count = 0
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)
            visits.discard((r,c))
            return count
        
        count = dfs(0, 0)
        return count
