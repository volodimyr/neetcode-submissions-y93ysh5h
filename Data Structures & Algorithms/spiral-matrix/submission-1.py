class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        N = ROWS*COLS

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = j = dr = 0
        visit = set()
        res = []

        for _ in range(N):
            res.append(matrix[i][j])
            visit.add((i,j))

            ni, nj = directions[dr][0]+i, directions[dr][1]+j
            if min(nj,nj) < 0 or ni == ROWS or nj == COLS or (ni,nj) in visit:
                dr = (dr+1) % 4
                ni, nj = directions[dr][0]+i, directions[dr][1]+j
            
            i, j = ni, nj

        return res