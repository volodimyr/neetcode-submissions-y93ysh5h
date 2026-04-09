class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:        
        N = len(stones)
        res = [math.inf]
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, cur):
            if i == N:
                return abs(cur)
            else:
                return min(dfs(i+1, stones[i]+cur), dfs(i+1, stones[i]-cur))
        
        return dfs(0, 0)