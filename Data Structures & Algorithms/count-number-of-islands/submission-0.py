class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
    
        def complete_island(r: int, c: int):
            if r < 0 or c < 0:
                return
            if r == ROWS or c == COLS:
                return
            if (r, c) in visited:
                return
            if grid[r][c] == '0':
                return
            
            visited.add((r,c))
            complete_island(r+1, c)
            complete_island(r-1, c)
            complete_island(r, c+1)
            complete_island(r, c-1)
            

        count = 0
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    count+=1
                    complete_island(i, j)


        return count