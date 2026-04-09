class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def helper(i, stock):
            if i >= len(prices):
                return 0
            if (i,stock) in memo:
                return memo[(i,stock)]
            
            res = 0
            if stock:
                sell = helper(i+2, False) + prices[i]
                buy = helper(i+1, True)
                res = max(buy, sell)
            else:
                buy = helper(i+1, True) - prices[i]
                sell = helper(i+1, False)
                res = max(buy, sell)
            memo[(i,stock)] = res
            
            return res
        
        return helper(0, False)