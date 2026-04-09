class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perm = 0
        q = deque()
        visit = set()
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                if grid[i][j] == 1:
                    q.append((i,j))
                    break
        
        while q:
            row, col = q.popleft()
            if min(row, col) < 0:
                continue
            if row == ROWS or col == COLS:
                continue
            if (row,col) in visit:
                continue
            if grid[row][col] != 1:
                continue
            visit.add((row,col))
            perm += self.calculate(grid, row, col)
            q.append((row+1, col))
            q.append((row-1, col))
            q.append((row, col+1))
            q.append((row, col-1))

        return perm
    
    def calculate(self, grid: List[List[int]], row: int, col: int) -> int:
        p = 4
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for dr, dc in directions:
            if min(row+dr,col+dc) < 0:
                continue
            if row+dr == ROWS or col+dc == COLS:
                continue
            if grid[row+dr][col+dc] == 1:
                p-=1
        return p
