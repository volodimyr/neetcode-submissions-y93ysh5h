class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        m = 0
        for i in range(1, len(nums)):
            if nums[m] > nums[i]:
                m = i
        
        org = m
        while True:
            nex = m+1
            if nex == len(nums):
                nex = 0
            if nex == org:
                return True
            if nums[nex] >= nums[m]:
                m += 1
                if m == len(nums):
                    m = 0
                continue
            else:
                return False