class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def helper(i, cap):
            if i == len(profit):
                return 0
            mx = helper(i+1, cap)
            newCap = cap - weight[i]
            if newCap >= 0:
                mx = max(profit[i] + helper(i, newCap), mx)
            return mx
        return helper(0, capacity)
