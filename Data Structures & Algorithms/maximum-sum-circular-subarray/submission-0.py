class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        length = len(nums)
        maxsubarray = 0
        for start in range (length):
            id = start
            curmax = 0
            while True:
                curmax += nums[id]
                curmax = max(curmax, 0)
                maxsubarray = max(maxsubarray, curmax)
                id = (id+1)%length
                if id == start:
                    break
        if maxsubarray == 0:
            maxsubarray = max(nums)
        return maxsubarray