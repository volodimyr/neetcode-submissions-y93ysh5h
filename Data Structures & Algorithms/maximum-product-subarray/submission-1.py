class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        N = len(nums)
        for i in range(N):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i+1, N+1):
                if j != N:
                    cur *= nums[j]
                res = max(res, cur)
        

        
        return res