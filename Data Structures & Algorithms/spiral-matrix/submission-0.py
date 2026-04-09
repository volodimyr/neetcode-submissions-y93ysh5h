class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        N = ROWS*COLS

        drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visit = set()

        def change_direction(dr):
            dr+=1
            if dr == len(drs):
                dr = 0
            return dr
            
        def next(i, j, dr):
            dri, drj = drs[dr]
            if i+dri < 0 or j+drj < 0 or i+dri == ROWS or j+drj == COLS or (i+dri, j+drj) in visit:
                return next(i, j, change_direction(dr))

            return i+dri, j+drj ,dr

        j = -1
        i = dr = 0
        res = []
        while len(res) < N:
            i, j, dr = next(i, j, dr)
            visit.add((i,j))
            res.append(matrix[i][j])

        return res