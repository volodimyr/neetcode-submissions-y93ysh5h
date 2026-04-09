class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1]*(len(cost)+1)
        return min(self.climb(0, cost, memo), self.climb(1, cost, memo))
    
    def climb(self, i: int, cost: List[int], memo: List[int]) -> int:
        if i < len(cost):
            if memo[i] != -1:
                return memo[i]
            memo[i] = min(cost[i]+self.climb(i+1, cost, memo), cost[i]+self.climb(i+2, cost, memo))
            return memo[i]
        else:
            return 0

