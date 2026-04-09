class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, j):
            if i == len(nums):
                return 1
            if nums[i] <= nums[j]:
                return dfs(i+1, j)
            if (i, j) in cache:
                return cache[(i,j)]
            count = max(1+dfs(i+1, i), dfs(i+1, j))
            cache[(i,j)] = count
            return count
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i, i)) 
        return res