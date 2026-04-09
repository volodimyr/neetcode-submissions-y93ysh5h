class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n2 = n * n

        arr = [0] * (n2+1)
        for i in range(1, n2+1):
            arr[i] = 0
                
        for r in range(n):
            for c in range(n):
                arr[grid[r][c]] += 1
                
        ans = [-1, -1]
        for i in range(1, len(arr)):
            if arr[i] == 0:
                ans[1] = i
            if arr[i] == 2:
                ans[0] = i
        
        return ans