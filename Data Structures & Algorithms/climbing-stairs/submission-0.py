class Solution:
   def climbStairs(self, n: int) -> int:
      memo = [0]*(n+1)
      return self.climb(n, memo)
   
   def climb(self, n: int, memo: List[int]) -> int:
      if n <= 1:
         return 1
      if memo[n]:
         return memo[n]
      memo[n] = self.climb(n-1, memo) + self.climb(n-2, memo)
      return memo[n]