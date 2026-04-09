class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1,1]]
        if numRows == 2:
            return res

        for i in range(1, numRows-1):
            r, c = i, 0

            res1 = [1]
            while c < len(res[i])-1:
                res1.append(res[i][c] + res[i][c+1])
                c+=1
            
            res1.append(1)
            res.append(res1)
        
        return res
