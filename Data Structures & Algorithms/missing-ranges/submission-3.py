class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        start = lower
        for i in range(len(nums)):
            n = nums[i]
            if start <= n - 1:
                res.append([start, n - 1])
                
            start = n + 1
        
        if start <= upper:
            res.append([start, upper])
        
        return res
