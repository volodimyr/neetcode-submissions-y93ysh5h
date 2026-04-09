class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ones = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1]
        visit = set()

        for r, c in ones:
            rtop = r-1
            rbottom = r+1
            

            while rtop != -1 :
                if grid[rtop][c] == 1:
                    visit.add((rtop,c))
                rtop-=1
            
            while rbottom != ROWS:
                if grid[rbottom][c] == 1:
                    visit.add((rbottom,c))
                rbottom+=1
            
            cright = c+1
            cleft = c-1

            while cright != COLS:
                if grid[r][cright] == 1:
                    visit.add((r,cright))
                cright+=1

            while cleft != -1:
                if grid[r][cleft] == 1:
                    visit.add((r,cleft))
                cleft-=1
            

        return len(visit)