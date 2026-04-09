class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mx = max(nums)
        arr = [-1]*(mx+2)
        for n in nums:
            if n < 0:
                continue
            arr[n] = n
        
        sm = 1
        for i in range(1, len(arr)):
            if arr[i] == -1:
                return i
        
        return sm