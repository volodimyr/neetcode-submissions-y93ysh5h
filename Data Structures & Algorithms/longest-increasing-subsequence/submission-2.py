class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0
            if (i, prev) in cache:
                return cache[(i,prev)]

            count = 0
            if prev == -1 or nums[i] > nums[prev]:
                count = max(1+dfs(i+1, i), dfs(i+1, prev))
            else:
                count = dfs(i+1, prev)

            cache[(i,prev)] = count

            return count

        res = 0
        N = len(nums)
        for i in range(N):
            if res >= N-i:
                break
            res = max(res, dfs(i, -1)) 
        return res