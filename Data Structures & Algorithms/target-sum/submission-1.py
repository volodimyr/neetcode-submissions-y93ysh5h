class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i:int, eval: int) -> int:
            if i == len(nums):
                return 1 if eval == target else 0
            if (i,eval) in cache:
                return cache[(i,eval)]
            cache[(i, eval)] = dfs(i+1, eval-nums[i]) + dfs(i+1, eval+nums[i])
            
            return cache[(i, eval)]
            
        return dfs(0, 0)