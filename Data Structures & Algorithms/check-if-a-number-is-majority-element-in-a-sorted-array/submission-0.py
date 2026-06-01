class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        res = 0
        for n in nums:
            if target == n:
                res += 1
        
        return res > len(nums) / 2