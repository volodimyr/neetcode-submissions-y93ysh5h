class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        left = []
        right = []
        
        cur = 0
        for i in range(k):
            left.append(cur)
            cur += cp[i]
        left.append(cur)
        # left.reverse()

        cur = 0
        for i in range(len(cp)-1, len(cp)-k-1, -1):
            right.append(cur)
            cur += cp[i]
        right.append(cur)
        right.reverse()

        res = 0
        for i in range(len(right)):
            res = max(res, right[i]+left[i])
        
        # for i in range(len(left)):
        #     res = max(res, left[i]+right[i])

 
        return res