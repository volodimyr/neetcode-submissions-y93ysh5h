class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            arr = []
            for i in range(len(nums)):
                heapq.heappush(arr, [nums[i], i])
            
            index = heapq.heappop(arr)[1]
            nums[index] *= multiplier
        
        return nums