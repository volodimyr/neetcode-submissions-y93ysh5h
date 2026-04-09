class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums), 1):
            j = 0
            count = 0
            while j < len(nums):
                if j == i:
                    j+=1
                    continue
                if nums[i] == nums[j]:
                    count+=1
                    break
                j+=1
            if count == 0:
                return nums[i]
        return 0
        