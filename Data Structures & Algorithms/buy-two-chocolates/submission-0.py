class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        change=money
        for i in range(2):
            if change - prices[i] < 0:
                return money
            change -= prices[i]
        
        return change