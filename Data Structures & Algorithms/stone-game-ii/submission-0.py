class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, m, alice):
            if i == N:
                return 0
            total = 0
            res = 0 if alice else math.inf
            for j in range(1, 2 * m + 1):
                if j + i > N:
                    break
                total += piles[i + j - 1]
                if alice:
                    res = max(res, total + dfs(i+j, max(m, j), not alice))
                else:
                    res = min(res, dfs(i+j, max(m, j), not alice))
            
            return res
        return dfs(0, 1, True)