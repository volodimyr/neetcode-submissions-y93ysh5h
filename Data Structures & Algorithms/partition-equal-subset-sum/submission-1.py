class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        memo = {}
        def helper(i, target):
            if i == N:
                return target == 0
            
            return helper(i+1, target) or helper(i+1, target-nums[i])
        
        return helper(0, sum(nums) / 2)