class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        def helper(i, left, right):
            if i == N:
                if left == right:
                    return True
                return False
            
            if helper(i+1, nums[i]+left, right):
                return True
            if helper(i+1, left, right+nums[i]):
                return True
            return False
        
        return helper(0, 0, 0)