class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        visit = set()

        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visit.add((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        
        if fresh == 0:
            return fresh
        
        t = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                
                for dr, dc in [[1,0], [-1,0], [0, 1], [0, -1]]:
                    nr, nc = dr+r, dc+c
                    if min(nr, nc) < 0:
                        continue
                    if nr >= ROWS:
                        continue
                    if nc >= COLS:
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    if (nr,nc) in visit:
                        continue
                    visit.add((nr, nc))
                    q.append((nr,nc))
                    fresh -= 1

            t += 1
        
        if fresh > 0:
            return -1
        
        return t if t else -1
                