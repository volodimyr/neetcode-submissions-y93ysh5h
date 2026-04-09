class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def calc(start, finish):
            rob1, rob2 = 0, 0
            for i in range(start, finish, 1):
                rob1, rob2, = rob2, max(nums[i]+ rob1, rob2)
            return rob2

        return max(calc(0, len(nums)-1), calc(1, len(nums)))