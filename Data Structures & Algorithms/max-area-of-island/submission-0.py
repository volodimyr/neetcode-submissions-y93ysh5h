class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visits = set()
        def dfs(r: int, c: int) -> int:
            if min(r,c) < 0:
                return 0
            if r == ROWS or c == COLS:
                return 0
            if (r,c) in visits:
                return 0
            if grid[r][c] == 0:
                return 0
            visits.add((r,c))
            return 1+ dfs(r+1, c)+dfs(r-1,c)+dfs(r, c+1)+dfs(r, c-1)
        
        max_area = 0
        for row in range (ROWS):
            for col in range (COLS):
                if grid[row][col] == 1 and (row,col) not in visits:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area