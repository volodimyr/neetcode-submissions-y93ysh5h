class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range (len(nums)):
            if i-k >= 0 and q[0][0] == i-k:
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

            if i-k+1>=0:
                res.append(q[0][1])

        return res