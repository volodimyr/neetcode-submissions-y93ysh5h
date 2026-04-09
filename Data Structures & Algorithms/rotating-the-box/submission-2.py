class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            R = L = COLS-1
            while True:
                if L < 0:
                    break
                if grid[i][L] == '.':
                    L-=1
                    continue
                if grid[i][L] == '*':
                    L-=1
                    R = L
                    continue
                grid[i][L], grid[i][R] = grid[i][R], grid[i][L]
                L-=1
                R-=1

        res = []
        for c in range (len(grid[0])):
            col = []
            for r in range (len(grid)-1, -1, -1):
                col.append(grid[r][c])
            res.append(col)

        return res
