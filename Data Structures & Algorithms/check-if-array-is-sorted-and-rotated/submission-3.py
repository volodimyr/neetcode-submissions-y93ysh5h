class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        i = 1
        while i < N and nums[i-1] <= nums[i]:
            i += 1

        return nums[i:] + nums[:i] == sorted(nums)