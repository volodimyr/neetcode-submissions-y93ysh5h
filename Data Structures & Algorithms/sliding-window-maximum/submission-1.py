class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        cur = 0
        res = []
        for i in range (k):
            if not q:
                q.append((i, nums[i]))
            elif q[0][1] <= nums[i]:
                q.clear()
                q.append((i, nums[i]))
            else:
                while q and q[-1][1] <= nums[i]:
                    q.pop()
                q.append((i, nums[i]))
        
        res.append(q[0][1])

        for i in range (k, len(nums), 1):
            if q[0][0] == i-k:
                q.popleft()
            if not q:
                q.append((i, nums[i]))
            elif q[0][1] <= nums[i]:
                q.clear()
                q.append((i, nums[i]))
            else:
                while q and q[-1][1] <= nums[i]:
                    q.pop()
                q.append((i, nums[i]))
            res.append(q[0][1])

        return res
