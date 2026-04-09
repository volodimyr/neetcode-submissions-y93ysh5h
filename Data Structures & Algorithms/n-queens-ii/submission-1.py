

class Solution:
    def totalNQueens(self, n: int) -> int:
        arr = [['.' for _ in range(n)] for _ in range(n)]
                
        visitc = set()
        visitPosD = set()
        visitNegD = set()
        def helper(r):
            if r == n:
                return 1
            res = 0
            for c in range(n):
                if c not in visitc and r+c not in visitPosD and r-c not in visitNegD:
                    arr[r][c] = 'Q'
                    visitc.add(c)
                    visitPosD.add(r+c)
                    visitNegD.add(r-c)

                    res += helper(r+1)

                    arr[r][c] = '.'
                    visitc.remove(c)
                    visitPosD.remove(r+c)
                    visitNegD.remove(r-c)
            return res
        

        return helper(0)
