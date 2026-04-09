class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 2:
            return 1
        l, r = 1, n
        res = 0
        while l <= r:
            m = (l + r) // 2
            steps = (m * (m + 1)) // 2
            if steps > n:
                r = m - 1
            else:
                res = max(res, m)
                l = m + 1
        
        return res
