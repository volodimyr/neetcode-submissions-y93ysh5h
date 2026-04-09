class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        def jump(i):
            if i >= N-1:
                return True
            if nums[i] == 0:
                return False
            
            j = nums[i]
            while j > 0:
                if jump(i+j):
                    return True
                j-=1
            return False
        
        return jump(0)