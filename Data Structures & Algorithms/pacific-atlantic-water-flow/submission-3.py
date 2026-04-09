class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs(r, c, visited):
            visited.add((r,c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr+r, dc+c
                if min(nr,nc) < 0:
                    continue
                if nr == ROWS or nc == COLS:
                    continue
                if (nr, nc) in visited:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
            
        visited_pacific = set()
        for row in range(ROWS):
            dfs(row, 0, visited_pacific)
        for col in range(COLS):
            dfs(0, col, visited_pacific)
        
        visited_atlantic = set()
        for row in range(ROWS):
            dfs(row, COLS-1, visited_atlantic)
        for col in range(COLS):
            dfs(ROWS-1, col, visited_atlantic)
        
        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in visited_pacific and (row,col) in visited_atlantic:
                    res.append([row,col])
 
        return res