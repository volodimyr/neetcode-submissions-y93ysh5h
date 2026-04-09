class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        cur = 0
        for n in nums:
            if n == 1:
                cur+=1
            else:
                if cur > consec:
                    consec = cur
                cur = 0
        if cur > consec:
            return cur
        else:
            return consec