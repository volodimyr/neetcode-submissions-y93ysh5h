class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        if ROWS == 1:
            return mat[0][0]
        res = 0
        for r in range(ROWS):
            res += mat[r][r]
            if r != (ROWS-1-r):
                res += mat[r][ROWS-1-r]
        return res