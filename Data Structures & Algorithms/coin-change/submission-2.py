class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        cache = {}
        def helper(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            
            res = 1e9
            for c in coins:
                if amount-c >= 0:
                    res = min(res, 1+helper(amount-c))
            cache[amount] = res
            return res

        res = helper(amount)
        return -1 if res == 1e9 else res
