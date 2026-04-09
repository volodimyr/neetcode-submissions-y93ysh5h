class Solution:
    def numDecodings(self, s: str) -> int:
        m = {str(i): chr(ord('A') + i - 1) for i in range(1, 10)}
        m1 = {str(i): chr(ord('A') + i - 1) for i in range(10, 27)}

        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] not in m:
                return 0
            res = dfs(i+1)
            if i+1 <= len(s) and s[i:i+2] in m1:
                res += dfs(i+2)
            
            return res
        
        return dfs(0)