class Solution:
    def tribonacci(self, n: int) -> int:
        def dfs(n, memo):
            if n < 1:
                return 0
            if n == 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = dfs(n-1, memo) + dfs(n-2, memo) + dfs(n-3, memo)
            return memo[n]
        return dfs(n, {})