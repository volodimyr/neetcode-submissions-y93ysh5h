class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:        
        N = len(stones)
        res = [math.inf]

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, left, right):
            if i == N:
                res[0] = min(res[0], abs(left-right))
            else:
                dfs(i+1, stones[i]+left, right)
                dfs(i+1, left, stones[i]+right)
        
        dfs(0, 0, 0)
        return res[0]