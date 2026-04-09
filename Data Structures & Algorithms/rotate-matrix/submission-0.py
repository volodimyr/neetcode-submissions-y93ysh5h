class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        t, b = 0, N-1
        while t < b:
            for c in range(N):
                 matrix[t][c], matrix[b][c] = matrix[b][c], matrix[t][c]
            t+=1
            b-=1


        for r in range(N):
            for c in range(r+1, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        
        