class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}
        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if (a,i) in cache:
                return cache[(a,i)]
            res = 0
            if a >= coins[i]:
                res = dfs(i+1, a)
                res += dfs(i, a-coins[i])
            cache[(a,i)] = res
            return res

        return dfs(0, amount)