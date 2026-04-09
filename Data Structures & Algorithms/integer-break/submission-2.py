class Solution:
    def integerBreak(self, target: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(x):
            if x == 1:
                return 0
            
            res = 0
            for j in range(1, x):
                res = max(res, j * (x-j), j * dfs(x-j))
            
            return res
        
        return dfs(target)