class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = [['.' for _ in range(n)] for _ in range(n)]
                
        visitc = set()
        visitPosD = set()
        visitNegD = set()
        res = []
        def helper(r):
            if r == n:
                res.append([''.join(row) for row in arr])
                return
            for c in range(n):
                if c not in visitc and r+c not in visitPosD and r-c not in visitNegD:
                    arr[r][c] = 'Q'
                    visitc.add(c)
                    visitPosD.add(r+c)
                    visitNegD.add(r-c)

                    helper(r+1)

                    arr[r][c] = '.'
                    visitc.remove(c)
                    visitPosD.remove(r+c)
                    visitNegD.remove(r-c)
        
        helper(0)

        return res
