class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        m = {}
        for i in range(1, 27):
            m[i] = chr(ord('A') + i - 1)

        n = columnNumber
        res = ""
        while n > 0:
            if n < 27:
                res = m[n] + res
                break
                
            res = m[n % 26] + res
            n //= 26
        
        return res