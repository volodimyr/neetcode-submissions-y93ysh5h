class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(total):
            if total == 0:
                return 1
            count = 0
            for n in nums:
                if total-n >= 0:
                    count += dfs(total-n)
            return count
        
        return dfs(target)
