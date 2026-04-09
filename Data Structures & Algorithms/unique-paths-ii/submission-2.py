class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        def dfs(r: int, c: int, memo: {})->int:
            if min(r,c) < 0:
                return 0
            if r > ROWS-1 or c > COLS-1:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == ROWS-1 and c == COLS-1:
                return 1

            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)] = (dfs(r+1, c, memo) + dfs(r, c+1, memo))
            return memo[(r,c)]
            
        return dfs(0,0, {})