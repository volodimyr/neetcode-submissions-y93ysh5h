class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, prev):
            if i == len(costs):
                return 0
            res = math.inf
            for j in range(len(costs[i])):
                if j == prev:
                    continue
                res = min(res, costs[i][j] + dfs(i+1, j))

            return res

        return dfs(0, -1)