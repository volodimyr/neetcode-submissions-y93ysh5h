class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        memo = {}
        def helper(i, target):
            if i == N:
                return target == 0
            if (i,target) in memo:
                return memo[(i,target)]
            memo[(i,target)] = helper(i+1, target) or helper(i+1, target-nums[i])
            return memo[(i,target)]
        
        return helper(0, sum(nums) / 2)