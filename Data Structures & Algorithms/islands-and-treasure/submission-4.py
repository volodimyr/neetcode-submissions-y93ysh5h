class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for row in range (len(grid)):
            for col in range (len(grid[row])):
                if grid[row][col] == 0:
                    q.append((row, col))
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1,0], [0, 1], [0,-1]]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if min(nr, nc) < 0:
                    continue
                if nr == ROWS or nc == COLS:
                    continue
                if grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = grid[row][col]+1
                q.append((nr,nc))
        
