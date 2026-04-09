class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        while L < R:
            mid = L + (R-L) // 2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid+1] > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1

        return L