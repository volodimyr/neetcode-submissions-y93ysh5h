class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return nums[self.find(nums, 0, len(nums)-1)]
        
    
    def find(self, nums, L, R):
        if L >= R:
            return L
        mid = L + (R-L) // 2

        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return mid
        
        if mid % 2 == 0:
            if nums[mid] == nums[mid+1]:
                return self.find(nums, mid +1, R)
            else:
                return self.find(nums, L, mid-1)
        else:
            if nums[mid] == nums[mid-1]:
                return self.find(nums, mid+1, R)
            else:
                return self.find(nums, L, mid-1)