class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        minh = []
        maxh = []

        for n in nums:
            heapq.heappush(minh, n)
            heapq.heappush(maxh, -n)
        
        for i in range(0, len(nums), 2):
            nums[i] = heapq.heappop(minh)
            if i + 1 < len(nums):
                nums[i+1] = -heapq.heappop(maxh)
