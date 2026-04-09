class Solution:
    def numDecodings(self, s: str) -> int:
        ch1 = {str(i) for i in range(1, 10)}   
        ch2 = {str(i) for i in range(10, 27)}

        cache = {}
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] not in ch1:
                return 0
            if i in cache:
                return cache[i]
            res = dfs(i+1)
            if i+1 <= len(s) and s[i:i+2] in ch2:
                res += dfs(i+2)
            cache[i] = res
            return res
        
        return dfs(0)