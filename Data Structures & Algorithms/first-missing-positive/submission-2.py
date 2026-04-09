class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # crazy solution with O(max(nums)) space complexity :D
        # mx = max(nums)
        # arr = [-1]*(mx+2)
        # for n in nums:
        #     if n < 0:
        #         continue
        #     arr[n] = n
        
        # sm = 1
        # for i in range(1, len(arr)):
        #     if arr[i] == -1:
        #         return i

        # a little better but still not O(1) space
        # ex = set()
        # mx = 1
        # for n in nums:
        #     if n < 1:
        #         continue
        #     mx = max(mx, n)
        #     ex.add(n)
        
        # for n in range(1, mx+2):
        #     if n not in ex:
        #         return n

        size = len(nums)
        for i in range(size):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(size):
            val = abs(nums[i])
            if val >= 1 and val <= size:
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (size+1)
        
        for i in range(1, size+1):
            if nums[i-1] >= 0:
                return i
                
        return size+1

            

