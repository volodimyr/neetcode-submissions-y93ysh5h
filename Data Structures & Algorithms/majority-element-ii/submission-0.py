class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = len(nums) // 3
        res = set()
        mcount = {}
        for n in nums:
            count = mcount.get(n, 0) + 1
            if count > times:
                res.add(n)
            mcount[n] = count
        return list(res)