class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0
            if (i, prev) in cache:
                return cache[(i,prev)]

            count = dfs(i+1, prev)
            if prev == -1 or nums[i] > nums[prev]:
                count = max(1+dfs(i+1, i), count)

            cache[(i,prev)] = count

            return count
        
        return dfs(0, -1)