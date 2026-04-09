class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.dfs(0, nums, {})
    
    def dfs(self, i: int, nums: List[int], memo: dict) -> int:
        if i > len(nums)-1:
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(nums[i] + self.dfs(i+2, nums, memo), self.dfs(i+1, nums, memo))
        return memo[i]
        