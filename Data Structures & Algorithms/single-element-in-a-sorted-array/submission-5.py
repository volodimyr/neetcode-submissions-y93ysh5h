class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        while L < R:
            mid = L + (R-L) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    L = mid +1
                else:
                    R = mid -1
            else:
                if nums[mid] == nums[mid-1]:
                    L = mid + 1
                else:
                    R = mid-1
        return nums[L]