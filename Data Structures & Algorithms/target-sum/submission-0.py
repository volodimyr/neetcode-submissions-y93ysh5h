class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i:int, eval: int) -> int:
            if i == len(nums):
                if eval == target:
                    return 1
                return 0
            
            return dfs(i+1, eval-nums[i]) + dfs(i+1, eval+nums[i])
            
        

        return dfs(0, 0)