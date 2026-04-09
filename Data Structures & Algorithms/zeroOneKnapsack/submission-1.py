class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = [[-1] * (capacity+1) for _ in range(len(profit))]
        
        def dfs(i, capacity) -> int:
            if i == len(profit):
                return 0
            if memo[i][capacity] != -1:
                return memo[i][capacity]

            memo[i][capacity] = dfs(i+1, capacity)

            new_cap = capacity - weight[i]
            if new_cap >= 0:
                p = profit[i] + dfs(i+1, new_cap)
                memo[i][capacity]  = max(memo[i][capacity], p)

            return memo[i][capacity]
        
        return dfs(0, capacity)