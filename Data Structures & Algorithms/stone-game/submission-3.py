class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        res = [0, 0]
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            odd = (j-i) % 2 == 1
            left = piles[i] if odd else 0
            right = piles[j] if odd else 0
            return max(dfs(i+1, j)+ left, dfs(i, j-1)+right)
        
        alice = dfs(0, len(piles)-1)
        total = sum(piles)

        return alice > (total - alice)


            