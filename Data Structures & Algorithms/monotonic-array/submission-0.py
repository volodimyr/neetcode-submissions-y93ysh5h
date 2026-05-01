class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        def increasing():
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    return False
            return True
        
        def decreasing():
            for i in range(1, len(nums)):
                if nums[i-1] < nums[i]:
                    return False
            return True
        
        if increasing():
            return True
        if decreasing():
            return True
        return False

                