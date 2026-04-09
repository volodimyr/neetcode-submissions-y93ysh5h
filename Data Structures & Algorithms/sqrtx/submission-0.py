class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        closest = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            q = mid * mid
            
            if q == x:
                return mid
            
            if q > x:
                right = mid - 1
            else:
                if mid > closest:
                    closest = mid
                left = mid + 1
        
        return closest