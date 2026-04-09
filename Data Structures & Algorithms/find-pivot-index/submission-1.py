class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        suffix = sum(nums[1:])
        
        prefix = 0
        for i in range(len(nums) - 1):
            if prefix == suffix:
                return i
            suffix -= nums[i + 1]
            prefix += nums[i]
        
        if prefix == suffix:
            return len(nums) - 1
        
        return -1