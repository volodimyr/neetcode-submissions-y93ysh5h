class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        treasure = 0
        land = 0
        for row in range (len(grid)):
            for col in range (len(grid[row])):
                if grid[row][col] == -1:
                    continue
                if grid[row][col] == 2147483647:
                    land += 1
                if grid[row][col] == 0:
                    treasure += 1
                    q.append((row, col))
        if treasure == 0:
            return
        if land == 0:
            return

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1,0], [0, 1], [0,-1]]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                if min(row+dr, col+dc) < 0:
                    continue
                if row+dr == ROWS or col+dc == COLS:
                    continue
                # if grid[row+dr][col+dc] == -1:
                #     continue
                # if grid[row+dr][col+dc] == 0:
                #     continue
                if grid[row+dr][col+dc] != 2147483647:
                    continue
                grid[row+dr][col+dc] = min(grid[row][col]+1, grid[row+dr][col+dc])
                q.append((row+dr,col+dc))
        
