class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [0]*(len(nums)+1)
        return self.dfs(0, nums, memo)
    
    def dfs(self, i: int, nums: List[int], memo: List[int]) -> int:
        if i > len(nums)-1:
            return 0
        if memo[i]:
            return memo[i]
        memo[i] = max(nums[i] + self.dfs(i+2, nums, memo), self.dfs(i+1, nums, memo))
        return memo[i]
        