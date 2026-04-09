class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        brk = -1
        for i in range(1, N):
            if nums[i-1] > nums[i]:
                brk = i
                break
        if brk == -1:
            return sorted(nums) == nums

        return nums[brk:] + nums[:brk] == sorted(nums)