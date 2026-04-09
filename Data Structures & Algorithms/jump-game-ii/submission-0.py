class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = math.inf
        def dfs(i, count):
            nonlocal res
            if i >= len(nums)-1:
                res = min(res, count)
            else:
                for j in range(1, nums[i]+1):
                    dfs(i+j, count+1)

        dfs(0, 0)
        return res