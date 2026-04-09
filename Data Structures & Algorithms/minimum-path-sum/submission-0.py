class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        from functools import lru_cache

        @lru_cache(None)
        def dfs(r, c):
            if min(r, c) < 0:
                return math.inf
            if r == ROWS or c == COLS:
                return math.inf
            if r == ROWS-1 and c == COLS-1:
                return grid[r][c]
            
            total = grid[r][c]
            return min(total+dfs(r+1,c), total + dfs(r, c+1))
        
        return dfs(0,0)