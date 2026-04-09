class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        min_len = float('inf')
        window = 0
        for R in range (len(nums)):
            window += nums[R]

            while window>=target:
                min_len = min(min_len, R-L+1)
                window -= nums[L]
                L+=1
            
        if min_len == float('inf'):
            return 0

        return min_len