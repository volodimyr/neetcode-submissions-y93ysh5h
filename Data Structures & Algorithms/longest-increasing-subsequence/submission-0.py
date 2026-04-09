class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, j):
            if i == len(nums):
                return 1
            if nums[i] <= nums[j]:
                return dfs(i+1, j)
            return max(1+dfs(i+1, i), dfs(i+1, j))
        
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i, i)) 
        return res