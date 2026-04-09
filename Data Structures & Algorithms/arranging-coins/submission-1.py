class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 2:
            return 1
        
        prev = 0
        cur = 0
        while prev + 1 + cur <= n:
            prev += 1
            cur += prev 
        
        return prev
