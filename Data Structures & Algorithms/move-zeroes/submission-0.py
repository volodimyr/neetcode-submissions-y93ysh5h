class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = R = 0
        while R < len(nums):
            if nums[R] == 0:
                R+=1
                continue
            nums[R], nums[L] = nums[L], nums[R]
            R+=1
            L+=1
        