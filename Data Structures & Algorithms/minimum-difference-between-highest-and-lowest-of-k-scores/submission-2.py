class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        if k == 1:
            return 0
        nums.sort()
        min_diff = nums[k-1]-nums[0]
        if min_diff == 0:
            return 0
        for i in range(k, len(nums), 1):
            min_diff = min(min_diff, nums[i]-nums[i-k+1])
            if min_diff == 0:
                return 0
        return min_diff