class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        length = 1
        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))

        while q:
            for i in range (len(q)):
                row, col = q.popleft()
                if row == ROWS-1 and col == COLS-1:
                    return length
                directions = [
                # diagonals
                    [-1,-1], [-1, 1], [1, -1], [1, 1], 
                # straight
                    [0, 1], [0, -1], [1, 0], [-1, 0]
                ]
                for dr, dc in directions:
                    if min(row + dr, col+dc) < 0:
                        continue
                    if row + dr == ROWS or col + dc == COLS:
                        continue
                    if (row+dr, col+dc) in visit:
                        continue
                    if grid[row+dr][col+dc] == 1:
                        continue
                    visit.add((row+dr,col+dc))
                    q.append((row+dr, col+dc))
            length+=1
        return -1