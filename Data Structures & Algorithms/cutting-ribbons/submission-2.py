class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
    
        def possible(x):
            count = 0
            for ribbon in ribbons:

                count += ribbon // x

                if count >= k:
                    return True
            
            return False
        
        ribbons.sort()

        L, R = 1, max(ribbons)
        res = 0
        while L <= R:

            mid = (L+R) // 2

            if possible(mid):
                L = mid + 1
                res = mid
            else:
                R = mid - 1
        
        return res