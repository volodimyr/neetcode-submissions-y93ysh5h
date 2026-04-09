class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            if q and q[0] <= i - k:
                q.popleft()
            if not q:
                q.append(i)
            elif nums[q[0]] <= nums[i]:
                q.clear()
                q.append(i)
            else:
                while q and nums[q[-1]] <= nums[i]:
                    q.pop()
                q.append(i)
            
            if i >= k - 1:
                res.append(nums[q[0]])

        return res