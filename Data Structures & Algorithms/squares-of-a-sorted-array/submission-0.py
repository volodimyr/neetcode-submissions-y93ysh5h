class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)

        L, R = 0, len(nums)-1
        i = len(nums)-1
        while L <= R:
            if abs(nums[L]) >= abs(nums[R]):
                res[i] = nums[L] * nums[L]
                L += 1
            else:
                res[i] = nums[R] * nums[R]
                R -=1
            i -= 1
        return res