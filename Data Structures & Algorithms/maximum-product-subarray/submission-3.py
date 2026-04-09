class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        N = len(nums)
        for i in range(N):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i+1, N):
                if j != N:
                    cur *= nums[j]
                res = max(res, cur)
        
        return res