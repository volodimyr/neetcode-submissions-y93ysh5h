class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zeroes = []
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zeroes.append((i,j))
        
        for i, j in zeroes:
            for row in range(ROWS):
                matrix[row][j] = 0
            for col in range(COLS):
                matrix[i][col]= 0