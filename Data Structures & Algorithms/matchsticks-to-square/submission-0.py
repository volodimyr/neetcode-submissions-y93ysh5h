class Solution:
    def makesquare(self, ms: List[int]) -> bool:
        summ = sum(ms)
        if summ % 4 != 0:
            return False
        N = len(ms)

        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, left, right, up, down):
            if i == N:
                return left == right == up == down
            
            for j in range(i, N):
                return (
                    dfs(j+1, left+ms[j], right, up, down) or
                    dfs(j+1, left, right+ms[j], up, down) or
                    dfs(j+1, left, right, up+ms[j], down) or
                    dfs(j+1, left, right, up, down+ms[j]))
        
        return dfs(0, 0, 0, 0, 0)