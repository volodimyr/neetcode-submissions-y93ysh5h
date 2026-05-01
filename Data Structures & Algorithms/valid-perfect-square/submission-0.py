class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        L, R = 1, num
        while L <= R:
            mid = (L+R) // 2
            n = mid * mid
            if n == num:
                return True
            
            if n > num:
                R = mid - 1
            else:
                L = mid + 1
        
        return False