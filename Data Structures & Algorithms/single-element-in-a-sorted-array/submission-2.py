class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        found = self.find(nums, 0, len(nums)-1)
        if found == -1:
            return found
        return nums[found]
        
    
    def find(self, nums, L, R):
        if L > R:
            return -1
        mid = L + (R-L) // 2
        if mid == 0 and nums[mid] != nums[mid+1]:
            return mid
        elif mid == len(nums)-1 and nums[mid] != nums[mid-1]:
            return mid
        elif nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return mid

        found = self.find(nums, mid+1, R)
        if found != -1:
            return found
        found = self.find(nums, L, mid-1)
        if found != -1:
            return found
        
        return -1