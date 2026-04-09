from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            v = nums[mid]

            if v == target:
                return mid
            if v < target:
                if mid + 1 > index:
                    index = mid + 1
                low = mid + 1
            else:
                high = mid - 1

        return index
