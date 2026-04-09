class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        h = []
        for i in range(1, nums[0]+1):
            heapq.heappush(h, (i, 1))
        
        N = len(nums)-1
        visited = set()
        while h:
            i, steps = heapq.heappop(h)
            visited.add(i)
            if i >= N:
                return steps

            for j in range(1, nums[i]+1):
                if (j+i) not in visited:
                    heapq.heappush(h, (j+i, steps+1))
        
        return -1

