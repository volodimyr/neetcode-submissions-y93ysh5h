class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        default = [['.' for _ in range(n)] for _ in range(n)]
                
        def col(c, matrix):
            for r in range(n):
                if matrix[r][c] == 'Q':
                    return False
            return True

        def diagonal(r, c, matrix, row=True, col=True):
            while True:
                if min(r, c) < 0 or max(r, c) >= n:
                    break
                if matrix[r][c] == 'Q':
                    return False
                if row:
                    r += 1
                else:
                    r -= 1
                if col:
                    c += 1
                else:
                    c -= 1

            return True
        
        def pack(arr):
            return [''.join(row) for row in arr]


        
        res = []
        def helper(r, arr):
            if r == n:
                res.append(pack(arr))
                return
            for c in range(n):
                if not (col(c, arr) and diagonal(r, c, arr) and diagonal(r, c, arr, False, False) and diagonal(r, c, arr, True, False) and diagonal(r, c, arr, False, True)):
                    continue
                arr[r][c] = 'Q'
                helper(r+1, arr)
                arr[r][c] = '.'
        
        helper(0, default)

        return res
