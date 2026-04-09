class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        memo = {}
        def jump(i):
            if i >= N-1:
                return True
            if i in memo:
                return memo[i]
            
            if nums[i] == 0:
                memo[i] = False
                return memo[i]
            
            j = nums[i]
            while j > 0:
                if jump(i + j):
                    memo[i] = True
                    return True
                j-=1

            memo[i] = False

            return memo[i]
        
        return jump(0)