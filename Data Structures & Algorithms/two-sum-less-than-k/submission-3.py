class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        end = -1
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= k:
                hi = mid - 1
            else:
                lo = mid + 1
                end = mid
        
        if end == -1 or end == 0:
            return -1
        
        res = -1
        for i in range(end, 0, -1):
            for j in range(i-1, -1, -1):
                if nums[i] + nums[j] < k:
                    res = max(res, nums[i]+nums[j])
        
        return res
