class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for row in range (len(grid)):
            for col in range (len(grid[row])):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col] == 1:
                    fresh+=1
        if fresh == 0:
            return 0
        minutes = 0
        ROWS, COLS = len(grid), len(grid[0])
        while q:
            rotten = False
            for i in range (len(q)):
                row, col = q.popleft()
                directions = [[1, 0], [-1,0], [0, 1], [0,-1]]
                for dr, dc in directions:
                    if min(row+dr, col+dc) < 0:
                        continue
                    if row+dr == ROWS or col+dc == COLS:
                        continue
                    if grid[row+dr][col+dc] != 1:
                        continue
                    grid[row+dr][col+dc] = 2
                    q.append((row+dr,col+dc))
                    rotten = True
                    fresh-=1
            if rotten:
                minutes+=1
        if fresh > 0:
            return -1
        return minutes
        