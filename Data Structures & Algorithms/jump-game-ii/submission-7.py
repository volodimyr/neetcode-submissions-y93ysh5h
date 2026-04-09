class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        L, R = 0, 0
        steps = 0

        while R < len(nums)-1:
            farthest = 0
            for i in range(L, R+1):
                farthest = max(farthest, i+nums[i])

            L = R+1
            R = farthest
            steps += 1
        
        return steps
