from functools import lru_cache


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        @lru_cache(None)
        def dfs(r, c):
            if r == N:
                return 0
            return min(triangle[r][c]+ dfs(r+1, c), triangle[r][c] + dfs(r+1, c+1))
        
        return dfs(0, 0)