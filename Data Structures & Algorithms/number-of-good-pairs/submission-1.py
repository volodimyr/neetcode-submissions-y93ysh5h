class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dup = {}
        res = 0
        for n in nums:
            if n not in dup:
                dup[n] = 1
            else:
                res += dup[n]
                dup[n] += 1
        return res
