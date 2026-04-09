class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        q = deque()
        for i in range(1, nums[0]+1):
            q.append((i, 1))
        
        N = len(nums)-1
        res = math.inf
        while q:
            i, steps = q.popleft()
            if i >= N:
                res = min(res, steps)
                continue
                
            for j in range(1, nums[i]+1):
                q.append((j+i, steps+1))
        
        return res

