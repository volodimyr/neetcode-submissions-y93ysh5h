class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zeroes = []
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zeroes.append((i,j))
        
        for i, j in zeroes:
            jleft = j
            jright = j
            while jleft != -1:
                matrix[i][jleft] = 0
                jleft-=1
                    
            while jright != COLS:
                matrix[i][jright] = 0
                jright+=1
                    
                itop = i
                idown = i

            while itop != -1:
                matrix[itop][j] = 0
                itop-=1 
                    
            while idown != ROWS:
                matrix[idown][j] = 0
                idown+=1
                
                
                
        