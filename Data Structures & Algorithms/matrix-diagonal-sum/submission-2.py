class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        if ROWS == 1:
            return mat[0][0]
        res = 0
        visit = set()
        for r in range(ROWS):
            res += mat[r][r]
            visit.add((r,r))
        c = 0
        for r in range(ROWS-1, -1, -1):
            if (r,c) not in visit:
                res += mat[r][c]
            c+=1
        return res