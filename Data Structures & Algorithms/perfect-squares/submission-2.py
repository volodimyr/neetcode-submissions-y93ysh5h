class Solution:
    def numSquares(self, target: int) -> int:

        memo = {}
        def helper(n):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            
            min_number = math.inf
            for i in range(1, target+1):
                if n-(i*i) >= 0:
                    min_number = min(1+helper(n-(i*i)), min_number)
            
            memo[n] = min_number
    
            return min_number
        

        
        return helper(target)
