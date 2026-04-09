class Solution:
    def numSquares(self, target: int) -> int:
        squares = [1]
        num = 2
        while True:
            tmp = num * num
            if tmp == target:
                return 1
            if tmp > target:
                break
            squares.append(tmp)
            num += 1
        
        memo = {}
        def helper(n):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            
            min_number = math.inf
            for s in squares:
                if n-s >= 0:
                    min_number = min(1+helper(n-s), min_number)
            
            memo[n] = min_number
    
            return min_number
        

        
        return helper(target)
