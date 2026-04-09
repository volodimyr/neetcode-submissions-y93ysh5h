class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        res = [0, 0]

        def dfs(i, j):
            if i >= j:
                return res[0] > res[1]
            res[0] += piles[i]
            res[1] += piles[j]
            if dfs(i+1, j-1):
                return True
            res[0] -= piles[i]
            res[1] -= piles[j]
            res[0] += piles[j]
            res[1] += piles[i]
            if dfs(i+1, j-1):
                return True
            res[0] -= piles[j]
            res[1] -= piles[i]
            res[0] += piles[j]
            res[1] += piles[j]
            if dfs(i, j-2):
                return True
            res[0] -= piles[j]
            res[1] -= piles[j]
            res[0] += piles[i]
            res[1] += piles[i]

            return dfs(i+2, j)
        
        return dfs(0, len(piles)-1)


            