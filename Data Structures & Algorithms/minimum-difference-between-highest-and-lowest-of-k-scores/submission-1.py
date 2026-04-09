class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        if k == 1:
            return 0
        nums.sort()
        min_diff = 0
        list = [0]*2
        list[0] = nums[0]
        list[1] = nums[k-1]
        min_diff = list[1]-list[0]
        if min_diff == 0:
            return 0
        for i in range(k, len(nums), 1):
            list[0], list[1] = nums[i-k+1], nums[i]
            min_diff = min(min_diff, list[1]-list[0])
            if min_diff == 0:
                return 0
        return min_diff
