class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = len(nums) // 3
        nums.sort()
        count = 1
        cur = nums[0]
        res = []
        for n in nums[1:]:
            if cur == n:
                count+=1
            else:
                if count > times:
                    res.append(cur)
                cur = n
                count = 1
        if count > times:
            res.append(cur)
        return res