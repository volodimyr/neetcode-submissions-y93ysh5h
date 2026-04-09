class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        summ, maxx = sum(nums), max(nums)
        if k == 1:
            return summ
        if len(nums) == k:
            return maxx
        L, R = maxx, summ
        minn = 0
        while L <= R:
            mid = L + (R-L) // 2
            times = 1
            total = 0
            for n in nums:
                if n + total > mid:
                    total = 0
                    times+=1
                total += n
                if times > k:
                    break
            if times > k:
                L = mid + 1
            else:
                minn = mid
                R = mid - 1
        return minn