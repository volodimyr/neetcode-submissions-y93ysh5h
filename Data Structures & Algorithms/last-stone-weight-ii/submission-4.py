class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:        
        N = len(stones)
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, left, right):
            if i == N:
                return abs(left-right)
            else:
                return min(dfs(i+1, left, stones[i]+right), dfs(i+1, stones[i]+left, right))
        
        return dfs(0, 0, 0)