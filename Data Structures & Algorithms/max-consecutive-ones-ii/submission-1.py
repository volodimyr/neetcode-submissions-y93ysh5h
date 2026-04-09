class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L = R = 0
        mx = 0
        skip = -1
        while R < len(nums):
            if nums[R] == 1:
                R+=1
            elif skip == -1:
                skip = R
                R+=1
            else:
                L = skip + 1
                skip = R
                R+=1
            mx = max(mx, R-L)        
        return mx