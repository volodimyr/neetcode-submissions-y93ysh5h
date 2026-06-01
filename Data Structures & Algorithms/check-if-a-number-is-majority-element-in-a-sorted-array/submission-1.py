class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:   
        L, R = 0, len(nums)-1
        index = -1
        while L <= R:
            mid = (L+R) // 2
            if nums[mid] >= target:
                R = mid - 1
                index = mid
            else:
                L = mid + 1
        
        half = len(nums) // 2
        if index == -1:
            return False
        
        if index + half >= len(nums):
            return False
        
        return nums[index+half] == target
        
        
