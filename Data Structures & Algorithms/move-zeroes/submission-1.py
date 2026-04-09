from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        for r in range(len(nums)):
            if nums[r]:
                if r != L:
                    nums[L], nums[r] = nums[r], nums[L]
                L+=1