class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [1] * (len(nums)+1)

        for n in nums:
            arr[n] -= 1
        
        res = []
        for i in range(1, len(arr)):
            a = arr[i]
            if a == 1:
                res.append(i)

        return res