class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r: int, c: int, memo: {})-> int:
            if min(r,c) < 0:
                return 0
            if r > m-1 or c > n-1:
                return 0
            if (r,c) in memo and memo[(r,c)] > 0:
                return memo[(r,c)]
            if r == m-1 and c == n-1:
                return 1
            memo[(r,c)] = (dfs(r+1, c, memo) + dfs(r, c+1, memo))
            return memo[(r,c)]
        return dfs(0, 0, {})
                